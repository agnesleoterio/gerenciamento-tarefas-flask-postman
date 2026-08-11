import tempfile
import unittest
from pathlib import Path

import app as app_module


class TaskApiTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        app_module.DB_PATH = Path(self.temp_dir.name) / "test_tasks.db"
        app_module.init_db()
        app_module.app.config["TESTING"] = True
        self.client = app_module.app.test_client()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_health_check_returns_ok(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_login_with_valid_credentials(self):
        response = self.client.post(
            "/login",
            json={"email": "ana@example.com", "password": "123456"},
        )

        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "login successful")
        self.assertEqual(data["user"]["email"], "ana@example.com")

    def test_login_with_wrong_credentials_returns_400(self):
        response = self.client.post(
            "/login",
            json={"email": "ana@example.com", "password": "wrong-password"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["message"], "wrong credentials")

    def test_login_without_password_returns_400(self):
        response = self.client.post("/login", json={"email": "ana@example.com"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["message"], "email and password are required")

    def test_create_task_with_valid_payload(self):
        response = self.client.post(
            "/tasks",
            json={
                "title": "Preparar entrevista Hays",
                "description": "Rever REST API e CI/CD",
                "status": "in progress",
                "priority": "high",
                "user_id": 1,
            },
        )

        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["title"], "Preparar entrevista Hays")
        self.assertEqual(data["status"], "in progress")
        self.assertEqual(data["priority"], "high")

    def test_list_and_get_existing_task(self):
        listed = self.client.get("/tasks")
        task_id = listed.get_json()[0]["id"]
        fetched = self.client.get(f"/tasks/{task_id}")

        self.assertEqual(listed.status_code, 200)
        self.assertGreater(len(listed.get_json()), 0)
        self.assertEqual(fetched.status_code, 200)
        self.assertEqual(fetched.get_json()["id"], task_id)

    def test_create_task_without_title_returns_400(self):
        response = self.client.post("/tasks", json={"status": "to do"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["message"], "title is required")

    def test_create_task_with_invalid_status_returns_400(self):
        response = self.client.post(
            "/tasks",
            json={"title": "Tarefa invalida", "status": "todo"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("status must be", response.get_json()["message"])

    def test_filter_tasks_by_status(self):
        response = self.client.get("/tasks?status=done")

        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data), 0)
        self.assertTrue(all(task["status"] == "done" for task in data))

    def test_get_missing_task_returns_404(self):
        response = self.client.get("/tasks/999")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["message"], "task not found")

    def test_update_and_delete_task(self):
        created = self.client.post("/tasks", json={"title": "Task temporaria"})
        task_id = created.get_json()["id"]

        updated = self.client.put(
            f"/tasks/{task_id}",
            json={"status": "done", "priority": "low"},
        )
        deleted = self.client.delete(f"/tasks/{task_id}")
        missing = self.client.get(f"/tasks/{task_id}")

        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.get_json()["status"], "done")
        self.assertEqual(deleted.status_code, 200)
        self.assertEqual(deleted.get_json()["message"], "task deleted")
        self.assertEqual(missing.status_code, 404)

    def test_reports_tasks_by_status(self):
        response = self.client.get("/reports/tasks-by-status")

        data = response.get_json()
        statuses = {item["status"] for item in data}
        self.assertEqual(response.status_code, 200)
        self.assertIn("done", statuses)
        self.assertIn("in progress", statuses)

    def test_reports_tasks_by_user(self):
        response = self.client.get("/reports/tasks-by-user")

        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual({item["user_name"] for item in data}, {"Ana", "Agatha"})

    def test_users_response_does_not_expose_passwords(self):
        response = self.client.get("/users")

        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(all("password" not in user for user in data))


if __name__ == "__main__":
    unittest.main()
