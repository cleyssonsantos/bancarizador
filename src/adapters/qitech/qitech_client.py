class QitechClient:
    def __init__(self):
        pass # Aqui ficaria a autenticação, toda vez que chamar o obj ele já chama autenticado

    def simular(self, payload: dict) -> dict:
        # Aqui seria uma chamada real à API do Qitech
        print(f"[Qitech] Simulando com payload: {payload}")
        return {
            "installment_amount": 150.75,
            "effective_rate": 1.82
        }
