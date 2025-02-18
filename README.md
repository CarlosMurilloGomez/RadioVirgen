Usuario:
  admin

Contraseña:
  1234
Comando 1(Diana): python manage.py cargaInicial
Comando 2(Carlos): python manage.py listarUsuarios
Comando 3(Diana): python manage.py listadoReproducciones <nickName>
Comando 4(Diana): python manage.py listaPendientes <nickName>, <id del podcast>


Comando 5(Iván):    python .\manage.py meGustaPodcast <nickName> --podcast_id <id del podcast>          -----De esta forma añades un podcast a un usuario
                    python .\manage.py meGustaPodcast <nickName>                          -----De esta otra, ves la lista de me gustas del usuario
Comando 6(Iván):    python manage.py anadirPodcastPendiente <nickName> --podcast_id <id>    -----Añade un podcast a la lista de pendientes


*en los commits he puesto comando 6 y comando 7; pero en verdad son el 7 y el 8, que me equivoqué
Comando 7(Carlos): python manage.py planPorUsuario <nickName>
Comando 8(Carlos): python manage.py ingresosUltimosMeses <nºMeses>