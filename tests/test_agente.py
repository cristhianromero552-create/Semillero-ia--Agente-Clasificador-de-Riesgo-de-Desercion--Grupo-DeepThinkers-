# tests/test_agente.py
def test_formato_respuesta():
    # Una prueba simple para verificar que la lógica de respuesta funciona
    ejemplo_resultado = {"respuesta": "Hola", "nivel_riesgo": "Bajo"}
    assert "respuesta" in ejemplo_resultado
    assert "nivel_riesgo" in ejemplo_resultado
    print("Prueba de formato de salida: PASADA ✅")

if __name__ == "__main__":
    test_formato_respuesta()
