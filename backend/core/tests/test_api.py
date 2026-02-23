from datetime import timedelta

from django.test import override_settings
from django.utils import timezone
from rest_framework.test import APITestCase

from core.models import Table, Quiz, Reservation


@override_settings(
    # da testovi ne zavise od realnog slanja mejla / resend konfiguracije
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
)
class ApiTests(APITestCase):
    def test_swagger_docs_works(self):
        resp = self.client.get("/api/docs/")
        self.assertEqual(resp.status_code, 200)

    def test_register_and_me(self):
        # register
        resp = self.client.post(
            "/api/auth/register/",
            data={
                "email": "test@example.com",
                "password": "testpass123",
                "password2": "testpass123",
            },
            format="json",
        )
        self.assertEqual(resp.status_code, 201, resp.data)
        self.assertIn("token", resp.data)

        # /me bez auth treba da odbije
        resp2 = self.client.get("/api/me/")
        self.assertIn(resp2.status_code, [401, 403])

        # /me sa auth treba da radi
        token = resp.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        resp3 = self.client.get("/api/me/")
        self.assertEqual(resp3.status_code, 200, resp3.data)
        self.assertEqual(resp3.data["email"], "test@example.com")

    def test_confirm_reservation_creates_row(self):
        # napravi user preko register, uzmi token
        reg = self.client.post(
            "/api/auth/register/",
            data={
                "email": "rez@example.com",
                "password": "testpass123",
                "password2": "testpass123",
            },
            format="json",
        )
        self.assertEqual(reg.status_code, 201, reg.data)
        token = reg.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        # pripremi minimalne podatke u bazi
        table = Table.objects.create(label="T1", capacity=4)
        quiz = Quiz.objects.create(
            name="Test Kviz",
            start_datetime=timezone.now() + timedelta(days=1),
        )

        # confirm rezervacije
        resp = self.client.post(
            "/api/reservations/confirm/",
            data={
                "quiz_id": quiz.id,
                "table_id": table.id,
                "team_name": "Tim Test",
                "party_size": 3,
            },
            format="json",
        )
        self.assertEqual(resp.status_code, 201, resp.data)

        # minimalna provera da je rezervacija stvarno kreirana u bazi
        self.assertTrue(
            Reservation.objects.filter(quiz=quiz, table=table, team_name="Tim Test").exists()
        )