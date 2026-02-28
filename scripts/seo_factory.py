import os

# CONFIGURACIÓN MAESTRA DE IDIOMAS Y KEYWORDS (Alto eCPM y Volumen)
estrategia_global = {
    "en": ["how to solve integrals step by step", "best AI for college students", "homework helper app free", "math solver with camera"],
    "de": ["mathe hausaufgaben hilfe ki", "physik aufgaben lösen app", "beste lern app für studenten", "integralrechnung rechner"],
    "fr": ["aide aux devoirs intelligence artificielle", "résoudre exercice de math gratuito", "meilleure application pour réviser", "calculatrice intégrale ia"],
    "pt": ["resolver exercícios de matemática ia", "melhor app para estudar engenharia", "ajuda com dever de casa gratis", "ia que resolve calculo"],
    "it": ["risolvere problemi di matematica gratis", "migliore app per studenti universitari", "intelligenza artificiale per studiare"],
    "jp": ["数学 問題 解き方 AI", "大学 勉強 アプリ おすすめ", "積分 計算機 アプリ", "AI 宿題 ヘルパー"],
    "kr": ["수학 문제 풀이 AI", "대학생 공부 필수 앱", "물리 문제 해결사", "가장 좋은 숙제 도움 앱"],
    "es": ["como resolver derivadas paso a paso", "mejor ia para hacer tareas", "ejercicios de algebra resueltos", "app para estudiar gratis"]
}

# CONTENIDO EXPANDIDO POR IDIOMA (Persuasión de ventas)
textos = {
    "en": {"h1": "Struggling with homework?", "desc": "Educare AI is the most advanced tool for students. Solve complex problems in seconds with detailed explanations.", "btn": "GET IT ON PLAY STORE", "benefit": "✓ Fast ✓ Precise ✓ 24/7 Support"},
    "de": {"h1": "Probleme bei den Hausaufgaben?", "desc": "Educare AI ist das fortschrittlichste Tool für Studenten. Lösen Sie komplexe Probleme in Sekunden mit Erklärungen.", "btn": "IM PLAY STORE HERUNTERLADEN", "benefit": "✓ Schnell ✓ Präzise ✓ 24/7 Hilfe"},
    "fr": {"h1": "Besoin d'aide pour vos devoirs ?", "desc": "Educare AI est l'outil le plus avancé pour les étudiants. Résolvez des problèmes complexes en quelques secondes.", "btn": "DISPONIBLE SUR PLAY STORE", "benefit": "✓ Rapide ✓ Précis ✓ Aide 24/7"},
    "pt": {"h1": "Dificuldade com os estudos?", "desc": "Educare AI é a ferramenta mais avançada. Resolva problemas complexos em segundos com explicações detalladas.", "btn": "BAIXAR NA PLAY STORE", "benefit": "✓ Rápido ✓ Preciso ✓ Suporte 24/7"},
    "it": {"h1": "Problemi con i compiti?", "desc": "Educare AI è lo strumento più avanzato per gli studenti. Risolvi problemi complessi in pochi secondi.", "btn": "SCARICA SU PLAY STORE", "benefit": "✓ Veloce ✓ Preciso ✓ Supporto 24/7"},
    "jp": {"h1": "勉強でお困りですか？", "desc": "Educare AIは、学生向けの最も先進的なツールです。複雑な問題を数秒で解決し、詳細な説明を提供します。", "btn": "Playストアで入手", "benefit": "✓ 高速 ✓ 正確 ✓ 24時間サポート"},
    "kr": {"h1": "숙제가 어려우신가요?", "desc": "Educare AI는 학생들을 위한 가장 진보된 도구입니다. 복잡한 문제를 단 몇 초 만에 해결하고 상세한 설명을 제공합니다.", "btn": "Play 스토어에서 다운로드", "benefit": "✓ 신속함 ✓ 정확함 ✓ 24/7 지원"},
    "es": {"h1": "¿Problemas con tus tareas?", "desc": "Educare AI es la herramienta más avanzada para estudiantes. Resuelve problemas complejos en segundos con explicaciones.", "btn": "DESCARGAR EN PLAY STORE", "benefit": "✓ Rápido ✓ Preciso ✓ Soporte 24/7"}
}

def fabricar_paginas_globales():
    base_dir = os.path.expanduser('~/EducareAI_Project/web_seo_global')
    if not os.path.exists(base_dir): os.makedirs(base_dir)

    for lang, temas in estrategia_global.items():
        ruta_idioma = os.path.join(base_dir, lang)
        if not os.path.exists(ruta_idioma): os.makedirs(ruta_idioma)

        for tema in temas:
            nombre_fichero = tema.replace(" ", "-").lower() + ".html"
            ruta_final = os.path.join(ruta_idioma, nombre_fichero)

            # ESTRUCTURA HTML5 PROFESIONAL CON SEO
            html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{tema} - {textos[lang]['desc']}">
    <title>{tema.upper()} | Educare AI Solution</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: auto; padding: 20px; background: #f9f9f9; }}
        .card {{ background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; }}
        h1 {{ color: #2c3e50; font-size: 2.5em; }}
        .keyword {{ color: #e67e22; font-weight: bold; }}
        .btn {{ display: inline-block; background: #2980b9; color: white; padding: 20px 40px; text-decoration: none; border-radius: 50px; font-weight: bold; margin-top: 30px; transition: 0.3s; }}
        .btn:hover {{ background: #3498db; transform: scale(1.05); }}
        .benefits {{ list-style: none; padding: 0; margin: 20px 0; display: flex; justify-content: center; gap: 20px; font-weight: bold; color: #27ae60; }}
    </style>
</head>
<body>
    <div class="card">
        <p>Topic: <span class="keyword">{tema}</span></p>
        <h1>{textos[lang]['h1']}</h1>
        <p style="font-size: 1.2em;">{textos[lang]['desc']}</p>
        <ul class="benefits">
            <li>{textos[lang]['benefit'].split(' ')[0]} {textos[lang]['benefit'].split(' ')[1]}</li>
            <li>{textos[lang]['benefit'].split(' ')[2]} {textos[lang]['benefit'].split(' ')[3]}</li>
            <li>{textos[lang]['benefit'].split(' ')[4]} {textos[lang]['benefit'].split(' ')[5]}</li>
        </ul>
        <a href="https://play.google.com/store/apps/details?id=com.educareai.app" class="btn">{textos[lang]['btn']}</a>
        <p style="margin-top: 50px; font-size: 0.8em; color: #999;">© 2024 Educare AI Global - High Performance Educational Tech</p>
    </div>
</body>
</html>"""
            with open(ruta_final, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"🌎 [{lang.upper()}] Creada: {nombre_fichero}")

if __name__ == "__main__":
    print("--- 🚀 INICIANDO FÁBRICA GLOBAL ELITE ---")
    fabricar_paginas_globales()
    print("--- ✅ SISTEMA LISTO PARA INDEXAR ---")
