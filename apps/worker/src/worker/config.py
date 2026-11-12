"""Configuration de l'agent de veille droit du travail (Europe et DOM)."""

AGENT_TITLE = "Veille droit du travail - Europe et DOM"
WORKFLOW_NAME = "veille-droit-travail-ue-dom"
DEFAULT_LIBRARY_ID = "01a1cff3-5f04-70b3-b433-67e2f85f7d67"
LLM_MODEL = "mistral-medium-latest"

DOM_KEYWORDS = [
    "outre-mer", "outremer", "ultrapériphérique", "guadeloupe", "martinique",
    "guyane", "la réunion", "réunion", "mayotte", "polynésie", "calédonie",
    "saint-pierre", "wallis", "saint-martin", "dom",
]

TRAVAIL_KEYWORDS = [
    "travail", "travailleur", "emploi", "licenciement", "salaire",
    "discrimination", "congé", "syndicat", "temps de travail", "égalité",
    "salarié", "dialogue social", "inspection du travail",
]

SOURCES = [
    {
        "name": "Commission européenne - Emploi, affaires sociales et inclusion",
        "url": "https://ec.europa.eu/social/rss.jsp?langId=fr&feedId=27",
        "kind": "rss",
        "max_items": 15,
    },
    {
        "name": "Cour de justice de l'UE - Communiqués de presse",
        "url": "https://curia.europa.eu/site/jcms/qua1_6621/fr/rss",
        "kind": "rss",
        "max_items": 12,
        "keywords": TRAVAIL_KEYWORDS,
    },
    {
        "name": "EUR-Lex - Journal officiel de l'UE",
        "url": "https://eur-lex.europa.eu/rss/oj.html",
        "kind": "rss",
        "max_items": 12,
        "keywords": TRAVAIL_KEYWORDS + DOM_KEYWORDS,
    },
    {
        "name": "Ministère du Travail - filtre outre-mer",
        "url": "https://travail-emploi.gouv.fr/rss.xml",
        "kind": "rss",
        "max_items": 12,
        "keywords": DOM_KEYWORDS,
    },
    {
        "name": "Bulletins officiels sociaux - filtre outre-mer",
        "url": "https://bulletins-officiels.social.gouv.fr/rss.xml",
        "kind": "rss",
        "max_items": 12,
        "keywords": DOM_KEYWORDS,
    },
    {
        "name": "Vie-publique.fr - Lois, filtre outre-mer",
        "url": "https://www.vie-publique.fr/lois-feeds.xml",
        "kind": "rss",
        "max_items": 12,
        "keywords": DOM_KEYWORDS,
    },
    {
        "name": "Vie-publique.fr - Actualités, filtre Europe",
        "url": "https://www.vie-publique.fr/actualites-feeds.xml",
        "kind": "rss",
        "max_items": 12,
        "keywords": [
            "europe", "européen", "union européenne", "directive",
            "cjue", "cour de justice", "commission européenne",
        ],
    },
]
