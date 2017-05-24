# CosmicDisease

Tout d’abord ce projet se fait en collaboration avec un ami diplômé des beaux arts, Morgan Patimo. Dans sa démarche artistique, on peut retrouver entre autre des dessins d’art contemporain comme celui-ci http://cargocollective.com/patimomorgan/Cosmic-Disease. 
L’idée de notre application est de générer des dessins comme celui-ci de manière aléatoire à partir d’une base de données constituée d’images des différents objets que l’on peut trouver sur ce dessin. L’application est pensée pour que n’importe qui puisse lui fournir une base de donnée de trois types d’objets différents et demander de générer un dessin aléatoire.  
 
Pour lancer l’application, on utilise directement le main; dans cosmic_disease_app on trouve tous les contrôles de la fenêtre principale et dans image_processing/ip_func, les algorithmes qui génèrent le dessin. Vous pouvez aussi voir un exemple de ce que cela donne avec une base de données de formes géométriques trouvées sur internet via l’image color_img.jpg (qui porte très mal son nom…). 
 
Par la suite je vais travailler sur la gestion de la base de données : y a t’il besoin de traiter les images en amont, de les tronquer (afin que la génération du dessin soit la plus rapide possible) ? Il faudra aussi jouer sur la transparence des images pour retranscrire au mieux la texture des outils utilisés pour dessiner les différentes formes. 

