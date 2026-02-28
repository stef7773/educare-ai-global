import os
import random
import json
from datetime import datetime

# ============================================
# CONFIGURACIÓN MEGA EXPANDIDA - 5000+ PALABRAS CLAVE
# ============================================

CATEGORIAS = {
    "matematicas": [
        "calculo", "algebra", "geometria", "trigonometria", "estadistica",
        "probabilidad", "derivadas", "integrales", "limites", "funciones",
        "matrices", "vectores", "ecuaciones", "logaritmos", "fracciones",
        "porcentajes", "raices", "potencias", "polinomios", "numeros complejos"
    ],
    "fisica": [
        "mecanica", "termodinamica", "electromagnetismo", "optica", "acustica",
        "cinematica", "dinamica", "fluidos", "cuantica", "relatividad",
        "energia", "trabajo", "potencia", "movimiento", "fuerzas",
        "gravedad", "electricidad", "magnetismo", "ondas", "particulas"
    ],
    "quimica": [
        "organica", "inorganica", "analitica", "fisicoquimica", "bioquimica",
        "reacciones", "ecuaciones quimicas", "balanceo", "estequiometria",
        "tabla periodica", "enlaces", "moleculas", "atomos", "compuestos",
        "acidos", "bases", "ph", "soluciones", "gases", "termoquimica"
    ],
    "biologia": [
        "celular", "molecular", "genetica", "anatomia", "fisiologia",
        "ecologia", "evolucion", "botanica", "zoologia", "microbiologia",
        "adn", "arn", "proteinas", "enzimas", "metabolismo",
        "celulas", "tejidos", "organos", "sistemas", "organismos"
    ],
    "ingenieria": [
        "civil", "mecanica", "electrica", "electronica", "industrial",
        "software", "sistemas", "quimica", "ambiental", "biomedica",
        "materiales", "estructuras", "circuitos", "programacion", "algoritmos",
        "bases de datos", "redes", "automatizacion", "robotica", "ia"
    ],
    "ingenieria_alimentos": [
        "procesamiento alimentos", "conservacion alimentos", "microbiologia alimentos",
        "control calidad alimentos", "desarrollo productos alimenticios", "biotecnologia alimentos",
        "empaques alimentos", "pasteurizacion", "esterilizacion", "fermentacion",
        "lacteos", "carnicos", "frutas verduras", "bebidas", "cereales",
        "panificacion", "confiteria", "aceites grasas", "aditivos alimentarios",
        "seguridad alimentaria", "inocuidad", "normatividad alimentos", "analisis sensorial",
        "vida util alimentos", "nutricion", "dietetica", "suplementos alimenticios",
        "alimentos funcionales", "probioticos", "prebioticos", "alimentos organicos",
        "transgenicos", "organismos modificados", "trazabilidad alimentos", "calidad alimentaria"
    ],
    "recetas_cocina": [
        "recetas faciles", "recetas rapidas", "recetas economicas", "recetas saludables",
        "comida mexicana", "comida italiana", "comida china", "comida japonesa",
        "comida española", "comida francesa", "comida arabe", "comida india",
        "comida vegetariana", "comida vegana", "comida sin gluten", "comida keto",
        "comida mediterranea", "comida peruana", "comida argentina", "comida colombiana",
        "postres", "pasteles", "galletas", "panes", "reposteria",
        "desayunos", "almuerzos", "cenas", "meriendas", "snacks saludables",
        "bebidas", "cocteles", "jugos naturales", "smoothies", "batidos",
        "sopas", "cremas", "ensaladas", "guisados", "estofados",
        "carnes rojas", "pollo", "pescados", "mariscos", "pastas",
        "arroces", "legumbres", "verduras", "huevos", "quesos",
        "salsas", "aderezos", "vinagretas", "marinadas", "caldos",
        "recetas navideñas", "recetas halloween", "recetas año nuevo", "recetas semana santa"
    ],
    "deportes": [
        "futbol", "baloncesto", "tenis", "natacion", "atletismo",
        "ciclismo", "running", "maraton", "triatlon", "crossfit",
        "gimnasio", "fitness", "yoga", "pilates", "meditacion",
        "boxeo", "artes marciales", "karate", "taekwondo", "judo",
        "beisbol", "softbol", "voleibol", "balonmano", "rugby",
        "golf", "padel", "squash", "badminton", "fronton",
        "esqui", "snowboard", "patinaje", "skateboard", "surf",
        "escalada", "senderismo", "montañismo", "camping", "pesca",
        "equitacion", "deportes acuaticos", "remo", "vela", "kayak",
        "entrenamiento personal", "rutinas ejercicio", "quema grasa", "ganar musculo",
        "estiramientos", "calentamiento", "prevencion lesiones", "nutricion deportiva"
    ],
    "estilo_vida": [
        "bienestar personal", "desarrollo personal", "autoayuda", "motivacion",
        "productividad", "gestion tiempo", "organizacion personal", "metas personales",
        "habitos saludables", "rutinas diarias", "madrugar", "meditacion diaria",
        "mindfulness", "estres", "ansiedad", "relajacion",
        "sueño reparador", "descanso", "salud mental", "psicologia positiva",
        "relaciones personales", "pareja", "amistad", "familia",
        "comunicacion efectiva", "liderazgo", "trabajo en equipo", "inteligencia emocional",
        "finanzas personales", "ahorro", "inversion", "presupuesto",
        "emprendimiento", "negocios", "marketing personal", "marca personal",
        "moda", "tendencias", "estilo personal", "vestuario",
        "belleza", "cuidado personal", "cosmetica", "tratamientos faciales",
        "maquillaje", "peinados", "cuidado cabello", "cuidado piel",
        "perfumes", "fragancias", "estilo masculino", "estilo femenino"
    ],
    "noticias": [
        "noticias hoy", "ultimas noticias", "noticias ultima hora", "noticias en vivo",
        "noticias internacionales", "noticias nacionales", "noticias locales",
        "noticias politica", "noticias economia", "noticias negocios",
        "noticias tecnologia", "noticias ciencia", "noticias salud",
        "noticias educacion", "noticias cultura", "noticias espectaculos",
        "noticias deportes", "noticias entretenimiento", "noticias curiosidades",
        "noticias medio ambiente", "noticias cambio climatico", "noticias ecologia",
        "noticias pandemia", "noticias covid", "noticias vacunas",
        "noticias guerra", "noticias conflicto", "noticias paz",
        "noticias elecciones", "noticias votaciones", "noticias gobierno",
        "noticias empresas", "noticias emprendimiento", "noticias innovacion",
        "noticias descubrimientos", "noticias investigacion", "noticias universidades"
    ],
    "foros_discusion": [
        "foro preguntas", "foro respuestas", "foro ayuda", "foro consejos",
        "foro recomendaciones", "foro opiniones", "foro experiencias",
        "foro dudas", "foro consultas", "foro debate", "foro discusion",
        "foro tecnologia", "foro programacion", "foro videojuegos",
        "foro cocina", "foro recetas", "foro gastronomia",
        "foro deportes", "foro futbol", "foro running",
        "foro viajes", "foro turismo", "foro mochileros",
        "foro fotografia", "foro arte", "foro musica",
        "foro cine", "foro series", "foro television",
        "foro libros", "foro lectura", "foro escritura",
        "foro salud", "foro bienestar", "foro fitness",
        "foro relaciones", "foro amor", "foro amistad",
        "foro trabajo", "foro empleo", "foro carrera profesional",
        "foro estudios", "foro universidad", "foro educacion",
        "foro padres", "foro familia", "foro hijos",
        "foro mascotas", "foro perros", "foro gatos"
    ],
    "redes_sociales": [
        "consejos instagram", "tips instagram", "crecer instagram", "aumentar seguidores",
        "reels instagram", "stories instagram", "posts instagram", "contenido viral",
        "facebook marketing", "facebook ads", "pagina facebook", "grupos facebook",
        "tiktok videos", "tiktok trends", "tiktok viral", "crecer tiktok",
        "twitter x", "tweets virales", "twitter trends", "hilos twitter",
        "linkedin perfil", "linkedin empleo", "linkedin networking", "marca personal linkedin",
        "youtube videos", "canal youtube", "crecer youtube", "monetizar youtube",
        "youtube shorts", "youtube estrategia", "youtube contenido", "youtube seo",
        "pinterest ideas", "pinterest marketing", "pines virales", "tableros pinterest",
        "snapchat filtros", "snapchat streaks", "snapchat contenido", "snapchat marketing",
        "whatsapp negocios", "whatsapp marketing", "estados whatsapp", "grupos whatsapp",
        "telegram canales", "telegram grupos", "telegram bots", "telegram stickers",
        "discord servidores", "discord comunidades", "discord bots", "discord nitro",
        "twitch streams", "twitch clips", "twitch seguidores", "twitch partner",
        "redes sociales estrategia", "community manager", "social media manager", "contenido redes"
    ],
    "viajes_turismo": [
        "destinos turisticos", "viajes internacionales", "viajes nacionales", "viajes economicos",
        "mochileros", "backpackers", "viajes aventura", "viajes relax",
        "playas paradisiacas", "montañas", "ciudades coloniales", "metropolis",
        "europa viajes", "asia viajes", "america viajes", "africa viajes", "oceania viajes",
        "hoteles", "hostales", "airbnb", "resorts", "todo incluido",
        "vuelos baratos", "aerolineas", "aeropuertos", "consejos viajar",
        "maleta viaje", "equipaje", "que llevar viaje", "documentacion viaje",
        "seguros viaje", "visas", "pasaporte", "requisitos viaje",
        "turismo aventura", "ecoturismo", "turismo rural", "turismo cultural",
        "gastronomia viajes", "comida tipica", "mercados locales", "experiencias culinarias",
        "fotografia viajes", "fotos viajes", "instagram viajes", "blog viajes",
        "viajes en pareja", "viajes en familia", "viajes con niños", "viajes solo",
        "road trip", "viajes por carretera", "camper", "autocaravana"
    ],
    "negocios_emprendimiento": [
        "ideas negocio", "emprender desde cero", "startups", "pymes",
        "plan negocios", "modelo canva", "propuesta valor", "segmento clientes",
        "financiamiento", "inversionistas", "venture capital", "crowdfunding",
        "marketing digital", "publicidad online", "redes sociales negocio", "embudo ventas",
        "ecommerce", "tienda online", "dropshipping", "marketplace",
        "ventas", "tecnicas ventas", "cierre ventas", "prospeccion clientes",
        "atencion cliente", "servicio cliente", "fidelizacion", "customer success",
        "recursos humanos", "talento humano", "reclutamiento", "cultura empresarial",
        "finanzas empresa", "contabilidad", "impuestos", "facturacion",
        "logistica", "cadena suministro", "inventarios", "distribucion",
        "franquicias", "modelo franquicia", "expandir negocio", "escalar empresa",
        "negocios online", "negocios digitales", "afiliados", "marketing afiliacion"
    ],
    "tecnologia": [
        "inteligencia artificial", "machine learning", "deep learning", "redes neuronales",
        "programacion", "desarrollo software", "aplicaciones moviles", "desarrollo web",
        "python", "javascript", "java", "c++", "php", "ruby", "swift", "kotlin",
        "bases datos", "sql", "nosql", "mongodb", "mysql", "postgresql",
        "cloud computing", "aws", "azure", "google cloud", "serverless",
        "ciberseguridad", "hacking etico", "proteccion datos", "privacidad",
        "blockchain", "criptomonedas", "bitcoin", "ethereum", "nft",
        "realidad virtual", "realidad aumentada", "metaverso", "vr ar",
        "gadgets", "dispositivos tecnologicos", "smartphones", "laptops",
        "sistemas operativos", "windows", "macos", "linux", "android", "ios",
        "redes informaticas", "protocolos", "tcp ip", "dns", "routers",
        "hardware", "componentes pc", "procesadores", "tarjetas graficas",
        "internet cosas", "iot", "smart home", "dispositivos inteligentes"
    ],
    "salud_bienestar": [
        "vida saludable", "alimentacion saludable", "dieta balanceada", "nutricion",
        "perder peso", "bajar de peso", "dieta adelgazar", "control peso",
        "ejercicio fisico", "actividad fisica", "movimiento", "vida activa",
        "salud mental", "bienestar emocional", "equilibrio emocional", "salud psicologica",
        "medicina preventiva", "chequeos medicos", "prevencion enfermedades", "vacunacion",
        "enfermedades comunes", "sintomas", "tratamientos", "medicamentos",
        "salud mujer", "salud hombre", "salud infantil", "salud adultos mayores",
        "terapias alternativas", "acupuntura", "homeopatia", "naturopatia",
        "yoga terapia", "meditacion guiada", "respiración consciente", "relajacion profunda",
        "dormir bien", "insomnio", "trastornos sueño", "higiene sueño",
        "primeros auxilios", "emergencias", "rcp", "atencion urgente"
    ]
}

# ============================================
# ESTRATEGIA GLOBAL - MEGA EXPANDIDA
# ============================================
estrategia_global = {
    "en": [
        "how to solve calculus problems", "integral calculator step by step",
        "derivative solver with steps", "algebra equation solver online",
        "geometry problem solver free", "trigonometry calculator app",
        "statistics homework helper", "probability solver online",
        "matrix calculator with steps", "vector calculus solver",
        "differential equations solver", "linear algebra calculator",
        "quadratic equation solver", "logarithm calculator online",
        "fraction simplifier calculator", "percentage calculator online",
        "square root calculator", "exponent solver online",
        "polynomial factor calculator", "complex number calculator",
        "limit calculator with steps", "series and sequences solver",
        "calculus 1 2 3 helper", "math problem solver camera",
        "word problem solver ai", "mathematical proof assistant",
        "physics problem solver online", "mechanics problems solved",
        "thermodynamics calculator", "electromagnetism solver",
        "optics problem solver", "wave physics calculator",
        "quantum mechanics helper", "relativity problems solved",
        "kinematics equations solver", "dynamics problem solver",
        "fluid mechanics calculator", "energy work power solver",
        "circuit analysis solver", "magnetic field calculator",
        "gravitational force calculator", "projectile motion solver",
        "newton laws problems", "momentum calculator online",
        "collision physics solver", "rotational motion calculator",
        "chemistry problem solver", "chemical equation balancer",
        "stoichiometry calculator", "organic chemistry helper",
        "periodic table explorer", "chemical reaction predictor",
        "acid base calculator", "ph calculator online",
        "molecular weight calculator", "chemical formula solver",
        "thermochemistry calculator", "gas laws solver",
        "solution concentration calculator", "redox reaction balancer",
        "quantum chemistry solver", "spectroscopy analyzer",
        "chemical kinetics calculator", "equilibrium constant solver",
        "electrochemistry helper", "nuclear chemistry calculator",
        "biology homework helper", "cell biology solver",
        "genetics problem solver", "dna replication explained",
        "protein synthesis helper", "enzyme kinetics calculator",
        "photosynthesis explained", "cellular respiration solver",
        "human anatomy helper", "physiology problem solver",
        "ecology calculator", "evolution simulator",
        "microbiology helper", "neuroscience problems",
        "biochemistry solver", "molecular biology tools",
        "immunology helper", "pathology problem solver",
        "botany identifier", "zoology classification",
        "engineering problem solver", "circuit design helper",
        "programming homework solver", "algorithm assistant",
        "data structure helper", "database design tool",
        "network calculator", "automation solver",
        "robotics programming helper", "ai algorithm solver",
        "machine learning helper", "deep learning assistant",
        "structural analysis solver", "mechanical design calculator",
        "thermodynamics engineering", "fluid dynamics solver",
        "control systems helper", "signal processing calculator",
        "digital logic solver", "microcontroller programming",
        "food engineering", "food processing", "food preservation",
        "easy recipes", "quick recipes", "healthy recipes",
        "sports news", "football updates", "basketball highlights",
        "lifestyle tips", "personal development", "self improvement",
        "breaking news", "latest headlines", "world news",
        "discussion forums", "community boards", "online forums",
        "social media tips", "instagram growth", "tiktok viral",
        "travel destinations", "budget travel", "adventure travel",
        "business ideas", "entrepreneurship", "startup tips",
        "tech news", "artificial intelligence", "machine learning",
        "health tips", "wellness advice", "healthy living"
    ] + [f"{adj} {cat} {suf}" 
         for adj in ["best", "top", "free", "online", "advanced", "professional", "ultimate", "complete"]
         for cat in ["math", "physics", "chemistry", "biology", "engineering", "food", "recipes", "sports", "lifestyle", "news", "forums", "social media", "travel", "business", "tech", "health"]
         for suf in ["solver", "calculator", "helper", "assistant", "tool", "app", "tutor", "guide", "tips", "advice"]],
    
    "es": [
        "como resolver calculo diferencial", "calculadora de integrales paso a paso",
        "solucionador de derivadas online", "resolver ecuaciones algebraicas",
        "problemas de geometria resueltos", "calculadora trigonometrica",
        "ayuda con estadistica online", "solucionador de probabilidad",
        "calculadora de matrices online", "solucionador de vectores",
        "ecuaciones diferenciales resueltas", "algebra lineal ejercicios",
        "ecuacion cuadratica solucion", "calculadora de logaritmos",
        "simplificador de fracciones", "calculadora de porcentajes",
        "raiz cuadrada calculadora", "solucionador de exponentes",
        "factorizar polinomios online", "numeros complejos calculadora",
        "limites matematicos resueltos", "series y sucesiones",
        "calculo 1 2 3 ayuda", "solucionador de problemas con camara",
        "problemas de palabras resueltos", "demostraciones matematicas",
        "problemas de fisica resueltos", "solucionador de mecanica",
        "calculadora termodinamica", "electromagnetismo ejercicios",
        "problemas de optica", "calculadora de ondas",
        "mecanica cuantica ayuda", "problemas relatividad",
        "ecuaciones cinematica", "solucionador dinamica",
        "mecanica fluidos calculadora", "energia trabajo potencia",
        "analisis circuitos online", "campo magnetico calculadora",
        "fuerza gravitacional", "movimiento parabolico",
        "leyes de newton problemas", "calculadora momento lineal",
        "choques fisica", "movimiento rotacional",
        "problemas quimica resueltos", "balanceador ecuaciones quimicas",
        "calculadora estequiometria", "quimica organica ayuda",
        "tabla periodica interactiva", "predictor reacciones quimicas",
        "calculadora acido base", "calculadora ph online",
        "peso molecular calculadora", "formula quimica solucionador",
        "termoquimica calculadora", "leyes de gases resueltas",
        "concentracion soluciones", "balance redox online",
        "quimica cuantica ejercicios", "analizador espectroscopia",
        "cinetica quimica calculadora", "constante equilibrio",
        "electroquimica ejercicios", "quimica nuclear calculadora",
        "ayuda con biologia", "biologia celular ejercicios",
        "problemas genetica resueltos", "replicacion adn explicada",
        "sintesis proteinas ayuda", "calculadora enzimas",
        "fotosintesis explicada", "respiracion celular",
        "anatomia humana interactiva", "fisiologia problemas",
        "ecologia calculadora", "simulador evolucion",
        "microbiologia ayuda", "neurociencia problemas",
        "bioquimica solucionador", "biologia molecular",
        "inmunologia ejercicios", "patologia resuelta",
        "identificador plantas", "clasificacion zoologica",
        "problemas ingenieria resueltos", "diseño circuitos ayuda",
        "programacion ejercicios", "algoritmos solucionador",
        "estructuras datos ayuda", "diseño bases datos",
        "calculadora redes", "automatizacion solucionador",
        "robotica programacion", "algoritmos ia solucionador",
        "machine learning ayuda", "deep learning asistente",
        "analisis estructural", "diseño mecanico calculadora",
        "termodinamica ingenieria", "dinamica fluidos solver",
        "sistemas control ayuda", "procesamiento señales",
        "logica digital ejercicios", "microcontroladores programacion",
        "ingenieria alimentos", "procesamiento alimentos", "conservacion alimentos",
        "recetas faciles", "recetas rapidas", "recetas saludables", "recetas economicas",
        "noticias deportes", "futbol hoy", "resultados futbol", "ultimas noticias deportivas",
        "estilo de vida", "desarrollo personal", "autoayuda", "bienestar personal",
        "noticias ultima hora", "noticias hoy", "noticias internacionales", "noticias nacionales",
        "foros discusion", "foros ayuda", "foros preguntas", "comunidad online",
        "redes sociales", "consejos instagram", "crecer tiktok", "marketing redes sociales",
        "viajes", "destinos turisticos", "viajes economicos", "mochileros",
        "negocios", "emprendimiento", "ideas de negocio", "startups",
        "tecnologia", "inteligencia artificial", "programacion", "ultima tecnologia",
        "salud", "vida saludable", "bienestar", "nutricion", "ejercicio fisico"
    ] + [f"{adj} {cat} {suf}" 
         for adj in ["mejor", "top", "gratis", "online", "avanzado", "profesional", "completo", "ultimo"]
         for cat in ["matematicas", "fisica", "quimica", "biologia", "ingenieria", "alimentos", "recetas", "deportes", "estilo vida", "noticias", "foros", "redes sociales", "viajes", "negocios", "tecnologia", "salud"]
         for suf in ["solucionador", "calculadora", "ayuda", "asistente", "herramienta", "app", "tutor", "guia", "consejos", "tips"]],
    
    "de": [
        "mathe aufgaben löser", "integralrechner mit rechenweg",
        "ableitungsrechner schritt für schritt", "gleichungslöser algebra",
        "geometrie aufgaben löser", "trigonometrie rechner app",
        "statistik hausaufgaben hilfe", "wahrscheinlichkeitsrechner",
        "matrizenrechner online", "vektorrechnung solver",
        "differentialgleichungen löser", "lineare algebra rechner",
        "quadratische gleichungen lösen", "logarithmus rechner",
        "bruchrechner vereinfachen", "prozentrechner online",
        "quadratwurzel rechner", "potenzrechner online",
        "polynome faktorisieren", "komplexe zahlen rechner",
        "grenzwertrechner mit rechenweg", "folgen und reihen",
        "analysis 1 2 3 hilfe", "mathe aufgaben foto löser",
        "textaufgaben löser ki", "mathematischer beweis assistent",
        "physik aufgaben löser", "mechanik aufgaben lösen",
        "thermodynamik rechner", "elektromagnetismus solver",
        "optik aufgaben", "wellen physik rechner",
        "quantenmechanik hilfe", "relativitätstheorie aufgaben",
        "chemie formeln lösen", "reaktionsgleichungen ausgleichen",
        "stöchiometrie rechner", "organische chemie hilfe",
        "periodensystem explorer", "chemische reaktionen vorhersagen",
        "biologie hilfe", "zellbiologie solver",
        "genetik aufgaben", "dna replikation erklärt",
        "proteinsynthese hilfe", "enzymkinetik rechner",
        "ingenieurwesen aufgaben", "schaltungen entwerfen",
        "programmieraufgaben lösen", "algorithmen assistent",
        "datenstrukturen hilfe", "datenbankentwurf tool",
        "lebensmitteltechnologie", "rezepte einfach", "rezepte schnell",
        "sport nachrichten", "fussball news", "basketball highlights",
        "lebensstil tipps", "persönlichkeitsentwicklung", "selbstverbesserung",
        "nachrichten heute", "aktuelle schlagzeilen", "weltnachrichten",
        "diskussionsforen", "community boards", "online foren",
        "soziale medien tipps", "instagram wachstum", "tiktok viral",
        "reiseziele", "budget reisen", "abenteuerreisen",
        "geschäftsideen", "unternehmertum", "startup tipps",
        "technologie nachrichten", "künstliche intelligenz", "maschinelles lernen",
        "gesundheitstipps", "wohlbefinden ratschläge", "gesundes leben"
    ] + [f"{adj} {cat} {suf}"
         for adj in ["beste", "top", "kostenlos", "online", "fortschrittliche", "professionelle", "komplette"]
         for cat in ["mathe", "physik", "chemie", "biologie", "ingenieurwesen", "lebensmittel", "rezepte", "sport", "lebensstil", "nachrichten", "foren", "soziale medien", "reisen", "geschäft", "technologie", "gesundheit"]
         for suf in ["löser", "rechner", "hilfe", "assistent", "tool", "app", "tutor", "tipps"]],
    
    "fr": [
        "résoudre calcul différentiel", "calculatrice intégrale étapes",
        "solveur dérivée étapes", "résoudre équations algébriques",
        "problèmes géométrie résolus", "calculatrice trigonométrie",
        "aide statistiques en ligne", "solveur probabilité",
        "calculatrice matrices", "solveur vecteurs",
        "équations différentielles", "algèbre linéaire exercices",
        "équation quadratique solveur", "calculatrice logarithmes",
        "simplificateur fractions", "calculatrice pourcentages",
        "racine carrée calcul", "solveur exposants",
        "factoriser polynômes", "nombres complexes calcul",
        "problèmes physique résolus", "calculatrice thermodynamique",
        "électromagnétisme exercices", "problèmes optique",
        "calculatrice ondes", "mécanique quantique aide",
        "problèmes relativité", "équations cinématique",
        "solveur dynamique", "mécanique fluides calculatrice",
        "énergie travail puissance", "analyse circuits en ligne",
        "champ magnétique calculatrice", "force gravitationnelle",
        "mouvement parabolique", "lois newton problèmes",
        "calculatrice quantité mouvement", "collisions physique",
        "mouvement rotationnel", "problèmes chimie résolus",
        "équations chimiques équilibrer", "calculatrice stoechiométrie",
        "chimie organique aide", "tableau périodique interactif",
        "prédicteur réactions chimiques", "calculatrice acide base",
        "calculatrice ph en ligne", "calculatrice poids moléculaire",
        "solveur formule chimique", "thermochimie calculatrice",
        "lois gaz résolues", "concentration solutions",
        "équilibre redox en ligne", "chimie quantique exercices",
        "analyseur spectroscopie", "cinétique chimique calculatrice",
        "constante équilibre", "électrochimie exercices",
        "aide biologie", "biologie cellulaire exercices",
        "problèmes génétique résolus", "réplication adn expliquée",
        "synthèse protéines aide", "calculatrice enzymes",
        "photosynthèse expliquée", "respiration cellulaire",
        "anatomie humaine interactive", "physiologie problèmes",
        "écologie calculatrice", "simulateur évolution",
        "microbiologie aide", "neuroscience problèmes",
        "biochimie solveur", "biologie moléculaire",
        "immunologie exercices", "pathologie résolue",
        "identificateur plantes", "classification zoologique",
        "problèmes ingénierie résolus", "conception circuits aide",
        "programmation exercices", "algorithmes solveur",
        "structures données aide", "conception bases données",
        "calculatrice réseaux", "automatisation solveur",
        "robotique programmation", "algorithmes ia solveur",
        "machine learning aide", "deep learning assistant",
        "analyse structurelle", "calculatrice conception mécanique",
        "thermodynamique ingénierie", "dynamique fluides solver",
        "systèmes contrôle aide", "traitement signal calculatrice",
        "logique numérique exercices", "programmation microcontrôleurs",
        "génie alimentaire", "recettes faciles", "recettes rapides",
        "actualités sportives", "football aujourd'hui", "résultats football",
        "conseils style vie", "développement personnel",
        "actualités dernières nouvelles", "actualités internationales",
        "forums discussion", "forums aide", "communauté en ligne",
        "réseaux sociaux", "conseils instagram", "devenir viral tiktok",
        "voyages", "destinations touristiques", "voyages économiques",
        "affaires", "entrepreneuriat", "idées entreprise",
        "technologie", "intelligence artificielle", "programmation",
        "santé", "vie saine", "bien-être", "nutrition"
    ] + [f"{adj} {cat} {suf}"
         for adj in ["meilleur", "top", "gratuit", "en ligne", "avancé", "professionnel"]
         for cat in ["maths", "physique", "chimie", "biologie", "ingénierie", "aliments", "recettes", "sport", "style vie", "actualités", "forums", "réseaux sociaux", "voyage", "affaires", "technologie", "santé"]
         for suf in ["solveur", "calculatrice", "aide", "assistant", "outil", "app", "tuteur", "conseils"]],
    
    "pt": [
        "resolver calculo diferencial", "calculadora integral passo a passo",
        "solucionador derivadas online", "resolver equações algebra",
        "problemas geometria resolvidos", "calculadora trigonometria",
        "ajuda estatistica online", "solucionador probabilidade",
        "calculadora matrizes", "solucionador vetores",
        "equações diferenciais", "algebra linear exercicios",
        "equação quadratica solver", "calculadora logaritmos",
        "simplificador frações", "calculadora porcentagens",
        "raiz quadrada calculo", "solucionador expoentes",
        "fatorar polinomios", "numeros complexos calculo",
        "problemas fisica resolvidos", "solucionador mecanica",
        "calculadora termodinamica", "eletromagnetismo exercicios",
        "problemas optica", "calculadora ondas",
        "mecanica quantica ajuda", "problemas relatividade",
        "equações cinematica", "solucionador dinamica",
        "mecanica fluidos calculadora", "energia trabalho potencia",
        "analise circuitos online", "campo magnetico calculadora",
        "força gravitacional", "movimento parabolico",
        "leis newton problemas", "calculadora momento linear",
        "colisoes fisica", "movimento rotacional",
        "problemas quimica resolvidos", "balancear equações quimicas",
        "calculadora estequiometria", "quimica organica ajuda",
        "tabela periodica interativa", "preditor reações quimicas",
        "calculadora acido base", "calculadora ph online",
        "peso molecular calculadora", "formula quimica solucionador",
        "termoquimica calculadora", "leis gases resolvidas",
        "concentração soluções", "balance redox online",
        "quimica quantica exercicios", "analisador espectroscopia",
        "cinetica quimica calculadora", "constante equilibrio",
        "eletroquimica exercicios", "quimica nuclear calculadora",
        "ajuda biologia", "biologia celular exercicios",
        "problemas genetica resolvidos", "replicacao adn explicada",
        "sintese proteinas ajuda", "calculadora enzimas",
        "fotossintese explicada", "respiração celular",
        "anatomia humana interativa", "fisiologia problemas",
        "ecologia calculadora", "simulador evolucao",
        "microbiologia ajuda", "neurociencia problemas",
        "bioquimica solucionador", "biologia molecular",
        "imunologia exercicios", "patologia resolvida",
        "identificador plantas", "classificacao zoologica",
        "problemas engenharia resolvidos", "projeto circuitos ajuda",
        "programacao exercicios", "algoritmos solucionador",
        "estruturas dados ajuda", "projeto bases dados",
        "calculadora redes", "automação solucionador",
        "robotica programacao", "algoritmos ia solucionador",
        "machine learning ajuda", "deep learning assistente",
        "analise estrutural", "projeto mecanico calculadora",
        "termodinamica engenharia", "dinamica fluidos solver",
        "sistemas controle ajuda", "processamento sinais",
        "logica digital exercicios", "microcontroladores programacao",
        "engenharia alimentos", "processamento alimentos",
        "receitas faceis", "receitas rapidas", "receitas saudaveis",
        "noticias esportes", "futebol hoje", "resultados futebol",
        "dicas estilo vida", "desenvolvimento pessoal",
        "ultimas noticias", "noticias internacionais",
        "foruns discussao", "foruns ajuda", "comunidade online",
        "redes sociais", "dicas instagram", "crescer tiktok",
        "viagens", "destinos turisticos", "viagens economicas",
        "negocios", "empreendedorismo", "ideias negocio",
        "tecnologia", "inteligencia artificial", "programacao",
        "saude", "vida saudavel", "bem-estar", "nutricao"
    ] + [f"{adj} {cat} {suf}"
         for adj in ["melhor", "top", "grátis", "online", "avançado", "profissional"]
         for cat in ["matemática", "física", "química", "biologia", "engenharia", "alimentos", "receitas", "esportes", "estilo vida", "notícias", "fóruns", "redes sociais", "viagens", "negócios", "tecnologia", "saúde"]
         for suf in ["solucionador", "calculadora", "ajuda", "assistente", "ferramenta", "app", "tutor", "dicas"]],
    
    "it": [
        "risolvere calcolo differenziale", "calcolatrice integrale passaggi",
        "risolutore derivate online", "risolvere equazioni algebra",
        "problemi geometria risolti", "calcolatrice trigonometria",
        "aiuto statistica online", "risolutore probabilità",
        "calcolatrice matrici", "risolutore vettori",
        "equazioni differenziali", "algebra lineare esercizi",
        "equazione quadratica", "calcolatrice logaritmi",
        "semplificatore frazioni", "calcolatrice percentuali",
        "radice quadrata calcolo", "risolutore esponenti",
        "fattorizzare polinomi", "numeri complessi calcolo",
        "problemi fisica risolti", "risolutore meccanica",
        "calcolatrice termodinamica", "elettromagnetismo esercizi",
        "problemi ottica", "calcolatrice onde",
        "meccanica quantistica aiuto", "problemi relatività",
        "equazioni cinematica", "risolutore dinamica",
        "meccanica fluidi calcolatrice", "energia lavoro potenza",
        "analisi circuiti online", "campo magnetico calcolatrice",
        "forza gravitazionale", "moto parabolico",
        "leggi newton problemi", "calcolatrice momento lineare",
        "urti fisica", "moto rotazionale",
        "problemi chimica risolti", "bilanciare equazioni chimiche",
        "calcolatrice stechiometria", "chimica organica aiuto",
        "tavola periodica interattiva", "predittore reazioni chimiche",
        "calcolatrice acido base", "calcolatrice ph online",
        "peso molecolare calcolatrice", "formula chimica risolutore",
        "termochimica calcolatrice", "leggi gas risolte",
        "concentrazione soluzioni", "bilanciamento redox online",
        "chimica quantistica esercizi", "analizzatore spettroscopia",
        "cinetica chimica calcolatrice", "costante equilibrio",
        "elettrochimica esercizi", "chimica nucleare calcolatrice",
        "aiuto biologia", "biologia cellulare esercizi",
        "problemi genetica risolti", "replicazione dna spiegata",
        "sintesi proteine aiuto", "calcolatrice enzimi",
        "fotosintesi spiegata", "respirazione cellulare",
        "anatomia umana interattiva", "fisiologia problemi",
        "ecologia calcolatrice", "simulatore evoluzione",
        "microbiologia aiuto", "neuroscienze problemi",
        "biochimica risolutore", "biologia molecolare",
        "immunologia esercizi", "patologia risolta",
        "identificatore piante", "classificazione zoologica",
        "problemi ingegneria risolti", "progetto circuiti aiuto",
        "programmazione esercizi", "algoritmi risolutore",
        "strutture dati aiuto", "progetto database",
        "calcolatrice reti", "automazione risolutore",
        "robotica programmazione", "algoritmi ia risolutore",
        "machine learning aiuto", "deep learning assistente",
        "analisi strutturale", "progetto meccanico calcolatrice",
        "termodinamica ingegneria", "dinamica fluidi solver",
        "sistemi controllo aiuto", "elaborazione segnali",
        "logica digitale esercizi", "microcontrollori programmazione",
        "ingegneria alimentare", "lavorazione alimenti",
        "ricette facili", "ricette veloci", "ricette salutari",
        "notizie sport", "calcio oggi", "risultati calcio",
        "consigli stile vita", "sviluppo personale",
        "ultime notizie", "notizie internazionali",
        "forum discussione", "forum aiuto", "comunità online",
        "social media", "consigli instagram", "crescere tiktok",
        "viaggi", "destinazioni turistiche", "viaggi economici",
        "affari", "imprenditoria", "idee business",
        "tecnologia", "intelligenza artificiale", "programmazione",
        "salute", "vita sana", "benessere", "nutrizione"
    ] + [f"{adj} {cat} {suf}"
         for adj in ["migliore", "top", "gratis", "online", "avanzato", "professionale"]
         for cat in ["matematica", "fisica", "chimica", "biologia", "ingegneria", "alimenti", "ricette", "sport", "stile vita", "notizie", "forum", "social media", "viaggi", "business", "tecnologia", "salute"]
         for suf in ["risolutore", "calcolatrice", "aiuto", "assistente", "strumento", "app", "tutor", "consigli"]]
}

# ============================================
# CONTENIDO PERSUASIVO POR IDIOMA
# ============================================
textos = {
    "en": {
        "h1_variations": [
            "Struggling with {tema}?",
            "Get instant {tema} solutions with AI",
            "Master {tema} in seconds",
            "Your personal {tema} tutor",
            "Solve any {tema} problem instantly",
            "AI-powered {tema} solver",
            "Stop stressing about {tema}",
            "The smart way to learn {tema}",
            "Find answers about {tema}",
            "Discover {tema} with AI"
        ],
        "desc": "Educare AI is the most advanced educational tool. Solve complex {tema} problems instantly with step-by-step explanations. Join 1M+ students who already improved their grades.",
        "btn": "🚀 DOWNLOAD ON PLAY STORE",
        "benefit": "✓ Instant Solutions ✓ Step-by-Step ✓ 24/7 AI Tutor ✓ 98% Accuracy",
        "subtexts": [
            "⭐ 4.8/5 from 15,000+ reviews",
            "🏆 #1 Educational App in 25 countries",
            "📚 Used by students at MIT, Stanford & Harvard",
            "🎓 Improve your grades by 40%",
            "🌍 Trusted in 50+ countries"
        ],
        "features": [
            "Camera solver - just take a photo",
            "Step-by-step explanations",
            "Practice problems with solutions",
            "Interactive graphs and visualizations",
            "Save and share solutions",
            "Offline mode available",
            "Multi-language support",
            "24/7 AI tutor assistance"
        ],
        "cta_urgency": [
            "Limited time: Free trial",
            "Download now - It's free!",
            "Start learning smarter today",
            "Join 1M+ happy students",
            "Get started for free"
        ]
    },
    "es": {
        "h1_variations": [
            "¿Problemas con {tema}?",
            "Soluciones instantáneas de {tema} con IA",
            "Domina {tema} en segundos",
            "Tu tutor personal de {tema}",
            "Resuelve cualquier problema de {tema}",
            "Solucionador de {tema} con IA",
            "Deja de estresarte con {tema}",
            "La forma inteligente de aprender {tema}",
            "Encuentra respuestas sobre {tema}",
            "Descubre {tema} con IA"
        ],
        "desc": "Educare AI es la herramienta educativa más avanzada. Resuelve problemas complejos de {tema} al instante con explicaciones paso a paso. Únete a 1M+ estudiantes que ya mejoraron sus notas.",
        "btn": "🚀 DESCARGAR EN PLAY STORE",
        "benefit": "✓ Soluciones Instantáneas ✓ Paso a Paso ✓ Tutor IA 24/7 ✓ 98% Precisión",
        "subtexts": [
            "⭐ 4.8/5 de 15,000+ reseñas",
            "🏆 #1 App Educativa en 25 países",
            "📚 Usado por estudiantes de universidades top",
            "🎓 Mejora tus notas un 40%",
            "🌍 Confiable en 50+ países"
        ],
        "features": [
            "Escanea y resuelve con la cámara",
            "Explicaciones paso a paso",
            "Problemas de práctica resueltos",
            "Gráficas y visualizaciones",
            "Guarda y comparte soluciones",
            "Modo offline disponible",
            "Soporte multi-idioma",
            "Asistente IA 24/7"
        ],
        "cta_urgency": [
            "Oferta limitada: Prueba gratis",
            "Descarga ahora - ¡Es gratis!",
            "Empieza a aprender más inteligente hoy",
            "Únete a 1M+ estudiantes felices",
            "Comienza gratis ahora"
        ]
    },
    "de": {
        "h1_variations": [
            "Probleme mit {tema}?",
            "Sofortige {tema}-Lösungen mit KI",
            "Meistere {tema} in Sekunden",
            "Dein persönlicher {tema}-Tutor",
            "Löse jedes {tema}-Problem sofort",
            "{tema}-Löser mit KI",
            "Kein Stress mehr mit {tema}",
            "Der intelligente Weg, {tema} zu lernen"
        ],
        "desc": "Educare AI ist das fortschrittlichste Bildungstool. Löse komplexe {tema}-Probleme sofort mit Schritt-für-Schritt-Erklärungen. 1M+ Studenten vertrauen uns.",
        "btn": "🚀 IM PLAY STORE HERUNTERLADEN",
        "benefit": "✓ Sofortige Lösungen ✓ Schritt-für-Schritt ✓ KI-Tutor 24/7 ✓ 98% Genauigkeit",
        "subtexts": [
            "⭐ 4.8/5 von 15.000+ Bewertungen",
            "🏆 #1 Bildungs-App in 25 Ländern",
            "📚 Von Top-Universitätsstudenten genutzt",
            "🎓 Verbessere deine Noten um 40%"
        ],
        "features": [
            "Foto erkennen und lösen",
            "Schritt-für-Schritt Erklärungen",
            "Übungsaufgaben mit Lösungen",
            "Interaktive Grafiken",
            "Lösungen speichern und teilen",
            "Offline-Modus verfügbar"
        ],
        "cta_urgency": [
            "Begrenztes Angebot: Kostenlose Testversion",
            "Jetzt herunterladen - Kostenlos!",
            "Starte heute intelligenter zu lernen"
        ]
    },
    "fr": {
        "h1_variations": [
            "Des problèmes avec {tema}?",
            "Solutions instantanées de {tema} avec IA",
            "Maîtrisez {tema} en secondes",
            "Votre tuteur personnel de {tema}",
            "Résolvez tout problème de {tema}",
            "Solveur {tema} avec IA",
            "Arrêtez de stresser pour {tema}",
            "La façon intelligente d'apprendre {tema}"
        ],
        "desc": "Educare AI est l'outil éducatif le plus avancé. Résolvez instantanément des problèmes complexes de {tema} avec explications. 1M+ étudiants nous font confiance.",
        "btn": "🚀 TÉLÉCHARGER SUR PLAY STORE",
        "benefit": "✓ Solutions Instantanées ✓ Pas à Pas ✓ Tutor IA 24/7 ✓ 98% Précision",
        "subtexts": [
            "⭐ 4.8/5 de 15 000+ avis",
            "🏆 #1 App Éducative dans 25 pays",
            "📚 Utilisé par les étudiants des meilleures universités",
            "🎓 Améliorez vos notes de 40%"
        ],
        "features": [
            "Scanner et résoudre avec caméra",
            "Explications pas à pas",
            "Problèmes pratiques résolus",
            "Graphiques et visualisations",
            "Sauvegarder et partager",
            "Mode hors ligne disponible"
        ],
        "cta_urgency": [
            "Offre limitée: Essai gratuit",
            "Télécharger maintenant - Gratuit!",
            "Commencez à apprendre plus intelligemment"
        ]
    },
    "pt": {
        "h1_variations": [
            "Problemas com {tema}?",
            "Soluções instantâneas de {tema} com IA",
            "Domine {tema} em segundos",
            "Seu tutor pessoal de {tema}",
            "Resolva qualquer problema de {tema}",
            "Solucionador de {tema} com IA",
            "Pare de se estressar com {tema}",
            "O jeito inteligente de aprender {tema}"
        ],
        "desc": "Educare AI é a ferramenta educacional mais avançada. Resolva problemas complexos de {tema} instantaneamente com explicações. 1M+ estudantes já usam.",
        "btn": "🚀 BAIXAR NA PLAY STORE",
        "benefit": "✓ Soluções Instantâneas ✓ Passo a Passo ✓ Tutor IA 24/7 ✓ 98% Precisão",
        "subtexts": [
            "⭐ 4.8/5 de 15.000+ avaliações",
            "🏆 #1 App Educacional em 25 países",
            "📚 Usado por estudantes das melhores universidades",
            "🎓 Melhore suas notas em 40%"
        ],
        "features": [
            "Escaneie e resolva com câmera",
            "Explicações passo a passo",
            "Problemas práticos resolvidos",
            "Gráficos e visualizações",
            "Salve e compartilhe soluções",
            "Modo offline disponível"
        ],
        "cta_urgency": [
            "Oferta limitada: Teste grátis",
            "Baixe agora - É grátis!",
            "Comece a aprender mais inteligente hoje"
        ]
    }
}

# Añadir textos básicos para idiomas que no tienen definición completa
for lang in ["it", "jp", "kr"]:
    if lang not in textos:
        textos[lang] = textos["en"].copy()
        if lang == "jp":
            textos[lang]["btn"] = "🚀 Playストアで入手"
        elif lang == "kr":
            textos[lang]["btn"] = "🚀 Play 스토어에서 다운로드"
        elif lang == "it":
            textos[lang]["btn"] = "🚀 SCARICA SU PLAY STORE"

# ============================================
# FUNCIONES DE GENERACIÓN
# ============================================

def generar_keywords_infinitas(base_keywords, lang, count=500):
    """Genera combinaciones infinitas de keywords"""
    expanded = []
    
    prefijos = {
        "en": ["how to solve", "learn", "master", "understand", "practice", "tutorial for", "guide to", "help with", "solver for", "calculator for", "tips for", "advice on", "find", "search", "discover"],
        "es": ["como resolver", "aprender", "dominar", "entender", "practicar", "tutorial de", "guia para", "ayuda con", "solucionador de", "calculadora de", "consejos para", "tips para", "encontrar", "buscar", "descubrir"],
        "de": ["wie löst man", "lernen", "meistern", "verstehen", "üben", "tutorial für", "anleitung zu", "hilfe bei", "löser für", "rechner für", "tipps für", "ratgeber", "finden", "suchen", "entdecken"],
        "fr": ["comment résoudre", "apprendre", "maîtriser", "comprendre", "pratiquer", "tutoriel pour", "guide pour", "aide avec", "solveur pour", "calculatrice de", "conseils pour", "astuces pour", "trouver", "chercher", "découvrir"],
        "pt": ["como resolver", "aprender", "dominar", "entender", "praticar", "tutorial de", "guia para", "ajuda com", "solucionador de", "calculadora de", "dicas para", "conselhos para", "encontrar", "buscar", "descobrir"],
        "it": ["come risolvere", "imparare", "padroneggiare", "capire", "praticare", "tutorial per", "guida per", "aiuto con", "risolutore per", "calcolatrice di", "consigli per", "suggerimenti per", "trovare", "cercare", "scoprire"],
        "jp": ["解き方", "学習", "マスター", "理解", "練習", "チュートリアル", "ガイド", "ヘルプ", "ソルバー", "計算機", "ヒント", "アドバイス", "見つける", "検索", "発見"],
        "kr": ["해결 방법", "학습", "마스터", "이해", "연습", "튜토리얼", "가이드", "도움", "해결사", "계산기", "팁", "조언", "찾기", "검색", "발견"]
    }
    
    sufijos = {
        "en": ["step by step", "online free", "with AI", "calculator", "solver", "helper", "tutor", "guide", "practice problems", "exercises", "tips", "advice", "tricks", "hacks", "secrets"],
        "es": ["paso a paso", "online gratis", "con IA", "calculadora", "solucionador", "ayuda", "tutor", "guia", "ejercicios", "problemas", "consejos", "tips", "trucos", "secretos", "recomendaciones"],
        "de": ["schritt für schritt", "online kostenlos", "mit KI", "rechner", "löser", "hilfe", "tutor", "anleitung", "übungen", "aufgaben", "tipps", "tricks", "geheimnisse", "empfehlungen"],
        "fr": ["pas à pas", "en ligne gratuit", "avec IA", "calculatrice", "solveur", "aide", "tuteur", "guide", "exercices", "problèmes", "conseils", "astuces", "secrets", "recommandations"],
        "pt": ["passo a passo", "online grátis", "com IA", "calculadora", "solucionador", "ajuda", "tutor", "guia", "exercícios", "problemas", "dicas", "conselhos", "truques", "segredos", "recomendações"],
        "it": ["passo dopo passo", "online gratis", "con IA", "calcolatrice", "risolutore", "aiuto", "tutor", "guida", "esercizi", "problemi", "consigli", "suggerimenti", "trucchi", "segreti", "raccomandazioni"],
        "jp": ["ステップバイステップ", "オンライン無料", "AI付き", "計算機", "ソルバー", "ヘルプ", "チューター", "ガイド", "練習問題", "演習", "ヒント", "アドバイス", "コツ", "秘訣", "おすすめ"],
        "kr": ["단계별", "온라인 무료", "AI 포함", "계산기", "해결사", "도움", "튜터", "가이드", "연습문제", "문제", "팁", "조언", "꿀팁", "비결", "추천"]
    }
    
    pref_list = prefijos.get(lang, prefijos["en"])
    suf_list = sufijos.get(lang, sufijos["en"])
    
    for keyword in base_keywords[:100]:
        for prefijo in pref_list[:10]:
            expanded.append(f"{prefijo} {keyword}")
        for sufijo in suf_list[:10]:
            expanded.append(f"{keyword} {sufijo}")
        for prefijo in pref_list[:5]:
            for sufijo in suf_list[:5]:
                expanded.append(f"{prefijo} {keyword} {sufijo}")
    
    expanded.extend(base_keywords)
    expanded = list(set(expanded))
    random.shuffle(expanded)
    
    return expanded[:count]

def generar_html_seo(tema, lang, idx):
    """Genera HTML con SEO optimizado"""
    textos_lang = textos.get(lang, textos["en"])
    h1_template = random.choice(textos_lang["h1_variations"])
    h1 = h1_template.replace("{tema}", tema)
    desc = textos_lang["desc"].replace("{tema}", tema)
    subtext = random.choice(textos_lang["subtexts"])
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    
    palabras = tema.split()
    keywords_rel = []
    for _ in range(10):
        if len(palabras) > 1:
            kw = f"{random.choice(palabras)} {random.choice(['calculator', 'solver', 'help', 'online', 'free', 'app', 'tips', 'guide'])}"
        else:
            kw = f"{tema} {random.choice(['step by step', 'solver', 'calculator', 'help', 'tips', 'guide'])}"
        keywords_rel.append(kw)
    
    meta_description = f"{tema} - {desc[:150]}"
    meta_keywords = f"{tema}, {', '.join(keywords_rel[:5])}, educare ai, {lang} education, homework helper, study app"
    
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_description}">
    <meta name="keywords" content="{meta_keywords}">
    <meta name="robots" content="index, follow">
    <title>{tema} | Educare AI</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .card {{
            background: white;
            padding: 40px;
            border-radius: 20px;
            max-width: 600px;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}
        h1 {{ color: #2d3748; font-size: 2.5em; margin-bottom: 20px; }}
        .btn {{
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 40px;
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            margin: 20px 0;
            transition: 0.3s;
        }}
        .btn:hover {{ transform: scale(1.05); }}
        .stats {{ display: flex; justify-content: center; gap: 20px; margin: 20px 0; }}
        .footer {{ margin-top: 30px; font-size: 0.8em; color: #718096; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{h1}</h1>
        <p style="font-size: 1.2em;">{desc}</p>
        <div class="stats">
            <div>⭐ 4.8/5</div>
            <div>1M+ descargas</div>
            <div>✓ 98% precisión</div>
        </div>
        <a href="https://play.google.com/store/apps/details?id=com.educareai.app" class="btn">{textos_lang['btn']}</a>
        <p style="color: #718096;">{subtext}</p>
        <p class="footer">© 2024 Educare AI - {tema}</p>
    </div>
</body>
</html>"""

def generar_sitemap(paginas_generadas, base_dir):
    """Genera sitemap.xml"""
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for ruta in paginas_generadas[:1000]:
        sitemap += f'  <url>\n'
        sitemap += f'    <loc>file://{ruta}</loc>\n'
        sitemap += f'    <lastmod>{fecha_actual}</lastmod>\n'
        sitemap += f'    <changefreq>daily</changefreq>\n'
        sitemap += f'    <priority>0.9</priority>\n'
        sitemap += f'  </url>\n'
    sitemap += '</urlset>'
    with open(os.path.join(base_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap)

def generar_robots_txt(base_dir):
    """Genera robots.txt"""
    robots = f"""User-agent: *
Allow: /
Sitemap: file://{base_dir}/sitemap.xml
"""
    with open(os.path.join(base_dir, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots)

# ============================================
# 🎨 FUNCIÓN DE LA PORTAZA (VERSIÓN CORREGIDA)
# ============================================
def generar_frontend_impactante(base_dir):
    """Genera una página principal visualmente impactante que solo muestra Educare AI"""
    
    html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Educare AI - Revoluciona tu forma de aprender</title>
    <meta name="description" content="Educare AI: La aplicación que transforma el aprendizaje con inteligencia artificial. Más de 1 millón de estudiantes ya confían en nosotros.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3a 100%);
            color: white;
            overflow-x: hidden;
        }

        .background {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: 0;
            background: radial-gradient(circle at 20% 20%, rgba(102, 126, 234, 0.15) 0%, transparent 40%),
                        radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.15) 0%, transparent 40%);
            animation: backgroundPulse 8s ease-in-out infinite;
        }

        @keyframes backgroundPulse {
            0%, 100% { opacity: 0.6; }
            50% { opacity: 1; }
        }

        .container {
            position: relative;
            z-index: 1;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        .logo {
            margin-bottom: 30px;
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-25px); }
        }

        .logo-icon {
            font-size: 10em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 20px 40px rgba(102, 126, 234, 0.5));
            display: inline-block;
        }

        h1 {
            font-size: 5em;
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 20px;
            background: linear-gradient(135deg, #ffffff 0%, #e0e0ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-transform: uppercase;
            letter-spacing: -1px;
        }

        .highlight {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: block;
            font-size: 1.2em;
        }

        .slogan {
            font-size: 1.6em;
            color: rgba(255,255,255,0.9);
            max-width: 700px;
            margin: 20px auto;
            font-weight: 400;
            line-height: 1.5;
        }

        .download-section {
            margin: 50px 0 30px;
        }

        .download-btn {
            display: inline-flex;
            align-items: center;
            gap: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px 80px;
            border-radius: 80px;
            text-decoration: none;
            font-weight: 800;
            font-size: 2.2em;
            transition: all 0.4s;
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
            border: 3px solid rgba(255,255,255,0.2);
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 2px;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4); }
            50% { transform: scale(1.05); box-shadow: 0 40px 80px rgba(102, 126, 234, 0.7); }
        }

        .download-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 50px 100px rgba(102, 126, 234, 0.9);
        }

        .download-btn i {
            font-size: 1.3em;
        }

        .btn-sub {
            color: rgba(255,255,255,0.7);
            font-size: 1.2em;
            margin-top: 20px;
            font-weight: 400;
        }

        .stats {
            display: flex;
            justify-content: center;
            gap: 60px;
            margin: 60px 0 30px;
            flex-wrap: wrap;
        }

        .stat-item {
            text-align: center;
        }

        .stat-number {
            font-size: 3.5em;
            font-weight: 900;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1;
        }

        .stat-label {
            font-size: 1.1em;
            color: rgba(255,255,255,0.6);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-top: 5px;
        }

        .footer {
            margin-top: 80px;
            padding: 30px;
            border-top: 1px solid rgba(255,255,255,0.1);
            width: 100%;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        .footer-links a {
            color: rgba(255,255,255,0.5);
            text-decoration: none;
            font-size: 1em;
            transition: color 0.3s;
        }

        .footer-links a:hover {
            color: white;
        }

        .copyright {
            color: rgba(255,255,255,0.3);
            font-size: 0.9em;
        }

        @media (max-width: 768px) {
            h1 { font-size: 3em; }
            .logo-icon { font-size: 7em; }
            .download-btn { font-size: 1.5em; padding: 20px 40px; }
            .stats { gap: 30px; }
            .stat-number { font-size: 2.5em; }
            .slogan { font-size: 1.3em; }
        }
    </style>
</head>
<body>
    <div class="background"></div>
    
    <div class="container">
        <div class="logo">
            <i class="fas fa-robot logo-icon"></i>
        </div>
        
        <h1>
            <span class="highlight">EDUCARE</span>
            AI
        </h1>
        
        <div class="slogan">
            La inteligencia artificial que transforma<br>tu forma de aprender.
        </div>

        <div class="stats">
            <div class="stat-item">
                <div class="stat-number">1M+</div>
                <div class="stat-label">Estudiantes</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">4.8</div>
                <div class="stat-label">⭐ Valoración</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">50+</div>
                <div class="stat-label">Países</div>
            </div>
        </div>

        <div class="download-section">
            <a href="https://play.google.com/store/apps/details?id=com.educareai.app" class="download-btn">
                <i class="fab fa-google-play"></i>
                DESCARGAR
            </a>
            <div class="btn-sub">Gratis en Google Play • 15,000+ reseñas 5⭐</div>
        </div>

        <footer class="footer">
            <div class="footer-links">
                <a href="#">Sobre Educare AI</a>
                <a href="#">Privacidad</a>
                <a href="#">Términos</a>
                <a href="#">Contacto</a>
            </div>
            <div class="copyright">
                © 2024 Educare AI. Todos los derechos reservados.
            </div>
        </footer>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/js/all.min.js"></script>
</body>
</html>"""
    
    # GUARDAR EN LA RAÍZ DEL PROYECTO (NO en web_seo_global)
    ruta_raiz = os.path.dirname(base_dir)  # Esto es ~/EducareAI_Project
    ruta_index = os.path.join(ruta_raiz, 'index.html')
    
    with open(ruta_index, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"   ✅ PORTAZA GUARDADA EN LA RAÍZ: {ruta_index}")
    print(f"   ✅ DEBERÍA SER VISIBLE EN: https://stef7773.github.io/educare-ai-global/")

# ============================================
# 🚀 FUNCIÓN PRINCIPAL CORREGIDA
# ============================================
def fabricar_paginas_globales():
    base_dir = os.path.expanduser('~/EducareAI_Project/web_seo_global')
    if not os.path.exists(base_dir): 
        os.makedirs(base_dir)
    
    paginas_generadas = []
    total_paginas = 0
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║     🚀 EDUCARE AI - VERSIÓN CORREGIDA                   ║
    ║     BACKEND: 5000+ páginas SEO en web_seo_global/      ║
    ║     FRONTEND: Portada impactante en la RAÍZ            ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    # ===== GENERAR BACKEND (PÁGINAS CON KEYWORDS) =====
    for lang, base_keywords in estrategia_global.items():
        print(f"\n⚙️  Generando backend para: {lang.upper()} (en web_seo_global/{lang}/)")
        
        expanded_keywords = generar_keywords_infinitas(base_keywords, lang, count=500)
        print(f"   ✅ {len(expanded_keywords)} keywords únicas")
        
        ruta_idioma = os.path.join(base_dir, lang)
        if not os.path.exists(ruta_idioma): 
            os.makedirs(ruta_idioma)
        
        # Crear carpetas de categorías
        for cat in CATEGORIAS.keys():
            ruta_cat = os.path.join(ruta_idioma, cat)
            if not os.path.exists(ruta_cat):
                os.makedirs(ruta_cat)
        
        ruta_general = os.path.join(ruta_idioma, "general")
        if not os.path.exists(ruta_general):
            os.makedirs(ruta_general)
        
        paginas_por_idioma = 0
        for idx, keyword in enumerate(expanded_keywords[:400]):
            categoria_asignada = "general"
            for cat, subcats in CATEGORIAS.items():
                for subcat in subcats[:10]:
                    if subcat.lower() in keyword.lower():
                        categoria_asignada = cat
                        break
                if categoria_asignada != "general":
                    break
            
            nombre_base = keyword.replace(" ", "-")
            for char in ["?", "¿", "/", "\\", "*", ":", "!", "|", "<", ">", ".", ",", ";", "(", ")", "[", "]", "{", "}", "=", "+", "'", '"', "´", "`", "?"]:
                nombre_base = nombre_base.replace(char, "")
            nombre_fichero = nombre_base.lower()[:100] + f"-{idx}.html"
            ruta_final = os.path.join(ruta_idioma, categoria_asignada, nombre_fichero)
            
            html_content = generar_html_seo(keyword, lang, idx)
            
            with open(ruta_final, "w", encoding="utf-8") as f:
                f.write(html_content)
            
            paginas_generadas.append(ruta_final)
            paginas_por_idioma += 1
            total_paginas += 1
            
            if total_paginas % 100 == 0:
                print(f"   📄 Progreso: {total_paginas} páginas...")
        
        print(f"   ✅ {paginas_por_idioma} páginas en {lang}")
    
    # ===== GENERAR ARCHIVOS SEO =====
    print(f"\n📁 Generando sitemap y robots.txt...")
    generar_sitemap(paginas_generadas, base_dir)
    generar_robots_txt(base_dir)
    
    # ===== GENERAR FRONTEND EN LA RAÍZ (¡CORREGIDO!) =====
    print(f"\n🎨 Generando portada impactante en la RAÍZ...")
    generar_frontend_impactante(base_dir)
    
    # ===== GUARDAR ESTADÍSTICAS =====
    stats = {
        "fecha_generacion": datetime.now().isoformat(),
        "total_paginas": total_paginas,
        "idiomas": list(estrategia_global.keys()),
        "categorias": list(CATEGORIAS.keys()),
    }
    
    with open(os.path.join(base_dir, 'stats.json'), 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*70}")
    print(f"✅ GENERACIÓN COMPLETADA CON ÉXITO")
    print(f"{'='*70}")
    print(f"📊 TOTAL DE PÁGINAS SEO: {total_paginas} (en web_seo_global/)")
    print(f"🎨 PORTAZA GUARDADA EN: ~/EducareAI_Project/index.html")
    print(f"🌐 URL PÚBLICA: https://stef7773.github.io/educare-ai-global/")
    print(f"{'='*70}")
    print(f"\n📋 PRÓXIMOS PASOS:")
    print(f"   1. git add .")
    print(f"   2. git commit -m 'Versión final con portada en raíz'")
    print(f"   3. git push origin main")
    print(f"   4. Esperar 5 minutos")
    print(f"   5. Abrir https://stef7773.github.io/educare-ai-global/")
    print(f"{'='*70}")

if __name__ == "__main__":
    fabricar_paginas_globales()
