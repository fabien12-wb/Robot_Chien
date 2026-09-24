from llm.llm_client import get_actions_from_llm

commande = "Mets-toi debout, va vers l'avant puis pivote vers la droite"

actions = get_actions_from_llm(commande)

print("Commande :", commande)
print("Réponse du LLM :", actions)