from fastapi.testclient import TestClient
from main import app

PREFIX = "/api/v1"
client = TestClient(app)

def test_fluxo_simulacao_e2e():
    response = client.post(f"{PREFIX}/oferta/simular", json={
        "valor": 1000,
        "parcelas": 12,
        "produto_id": "123989"
    })
    data = response.json()
    assert response.status_code == 200
    assert "taxa_efetiva" in data
