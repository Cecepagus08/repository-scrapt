#!/bin/bash

# Baca file repos.txt dan lakukan cloning setiap repository
while IFS= read -r repo; do
  git clone "$repo"
done < repos.txt
