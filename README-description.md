# Test-Hello-Watt

Vous retrouverez ici le desccriptif de ce que j'ai encodé.

1) Mise en place du Dashboard : 
	Mon dashboard présente une courbe représentant la consommation annuelle d'un client i. 
		/consumption/i présente la consommation de l'année 2019. Cependant il est possible, en bas de page, d'accéder à la consommation des autres années, on y trouve également la possibilité de retourner à la page principale.

2) Mise en place de la détection des chauffages électriques : 
	J'ai fait le choix de faire cette detection uniquement lors du chargement de la page /admin/clients. 

3) Mise en place de la détection d'un incident : 
	Je n'ai pas réussi à trouver une méthode permettant de détecter une réelle anomalie. D'abord on trouve une variation importante de la consommation pour tous les clients entre chaque année, ensuite en regardant dans les metadata, je ne trouvais pas cohérent les date d'anomalies relevées dans la base de donnée. 
	Si il fallait quand même la coder, j'ajouterais :
		- deux attributs au modèle Client, "has_anomaly" et "anomaly_date",
		- une methode qui comparerait pour un client donné sa consommation mensuelle entre chaque année
	Je placerai le test même moment que que le test pour le chauffage électrique. 

4) Affichage des détections dans la visualisation administrateur :
	Avec les attributs ajoutés, il n'y a besoin de rien ajouter, la détection de has_elec_heating et de has_anomaly se fait par clients_list.html. 