
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from principal.application.services.saludar_service import SaludarService

@csrf_exempt
def saludar(request):

    if request.method != "POST":
        return JsonResponse({"error": "Solo se permite POST"}, status=405)

    try:
        datos = json.loads(request.body)
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "JSON invalido"}, status=400)

    if not isinstance(datos, dict):
        return JsonResponse({"error": "Se espera un objeto JSON"}, status=400)

    nombre = datos.get("nombre")

    if not isinstance(nombre, str) or not nombre.strip():
        return JsonResponse({"error": "Nombre requerido"}, status=400)

    servicio = SaludarService()
    mensaje = servicio.saludar(nombre.strip())

    return JsonResponse({"mensaje": mensaje})
