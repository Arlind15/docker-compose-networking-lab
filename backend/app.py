from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import psycopg2


DB_HOST = "database"
DB_NAME = "homelab"
DB_USER = "homelab"
DB_PASSWORD = "homelab_password"


def get_database_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":

            response = {
                "status": "healthy",
                "service": "Python Backend API"
            }

            data = json.dumps(response).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

            return

        if self.path == "/api":

            try:
                connection = get_database_connection()
                cursor = connection.cursor()

                cursor.execute(
                    "SELECT id, name, status, port FROM services ORDER BY id;"
                )

                rows = cursor.fetchall()

                services = []

                for row in rows:
                    services.append({
                        "id": row[0],
                        "name": row[1],
                        "status": row[2],
                        "port": row[3]
                    })

                cursor.close()
                connection.close()

                response = {
                    "status": "ok",
                    "service": "Python Backend API",
                    "database": "PostgreSQL",
                    "services": services
                }

                data = json.dumps(response).encode()

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            except Exception as error:

                response = {
                    "status": "error",
                    "database_connection": "failed",
                    "error": str(error)
                }

                data = json.dumps(response).encode()

                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

        else:

            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 5000), APIHandler)

print("Backend API running on port 5000")

server.serve_forever()
