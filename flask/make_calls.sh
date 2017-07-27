#!/bin/bash

wget -qO- --post-data='phrase=Frase de prueba para busquedas&letters=aeiou' localhost:5000/search
wget -qO- --post-data='phrase=Frase de prueba para busquedas&letters=qwerty' localhost:5000/search
wget -qO- --post-data='phrase=Frase de prueba para busquedas&letters=qaz' localhost:5000/search
wget -qO- --post-data='phrase=Frase de prueba para busquedas&letters=wsx' localhost:5000/search
wget -qO- --post-data='phrase=El murcielago comio cardillo y tofu&letters=aeiou' localhost:5000/search
wget -qO- --post-data='phrase=Mi teclado es Dvorak&letters=qwerty' localhost:5000/search

echo "End"
