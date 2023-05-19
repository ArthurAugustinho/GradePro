from django.shortcuts import render, redirect
from .models import Materia, Periodo

def formulario(request):
    periodos = Periodo.objects.all()
    materias = Materia.objects.all()
    context = {'periodos': periodos, 'materias': materias}
    return render(request, 'calculadora/formulario.html', context)

def resultado(request):
    if request.method == 'POST':
        ciclo = int(request.POST.get('ciclo'))
        notas = {}

        for materia in Materia.objects.all():
            notas_materia = []
            for i in range(1, ciclo + 1):
                nota = request.POST.get(f'nota_materia_{materia.id}_ciclo_{i}')
                if nota:
                    notas_materia.append(float(nota))
            notas[materia] = notas_materia
        
        total_notas = 0
        total_ciclos = ciclo
        for materia, notas_materia in notas.items():
            total_notas += sum(notas_materia)
            if len(notas_materia) < ciclo:
                total_ciclos -= 1

        media_total = total_notas / total_ciclos if total_ciclos > 0 else 0
        media_passar = 60 - media_total
        media_prox_ciclos = 60 - (total_notas / ciclo) if ciclo > 0 else 0
        possibilidade_reprovar = media_total < 60

        context = {
            'media_total': media_total,
            'media_passar': media_passar,
            'media_prox_ciclos': media_prox_ciclos,
            'possibilidade_reprovar': possibilidade_reprovar
        }
        return render(request, 'calculadora/resultado.html', context)
    else:
        return redirect('calculadora:formulario')
