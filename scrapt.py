import requests

def fetch_and_save_repos(username, jumlah):
    
    api = f"https://api.github.com/users/{username}/repos?per_page={jumlah}"
    
    try:
        response = requests.get(api)
        response.raise_for_status()  # Akan menghasilkan error jika permintaan tidak berhasil

        data = response.json()
        repo_urls = [repo['html_url'] for repo in data]


        with open('repos.txt', 'w') as file:
            for url in repo_urls:
                file.write(f"{url}\n")
        print("\n".join(repo_urls))
        print("Link repositori berhasil disimpan ke repos.txt")

    except requests.exceptions.RequestException as e:
        print(f"data tidak di temukan")

# Panggil fungsi dengan username GitHub
username = input("Masukkan username GitHub: ")
jumlah = input("Masukkan jumlah yg ingin di ambil: ")
fetch_and_save_repos(username, jumlah)
