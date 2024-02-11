import concurrent.futures
import requests

def DownloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"MultiProcessingConcurrentFutureExe/files/file{name}.jpg","wb").write(response.content)
  print(f"Finished Downloading {name}")

  
if __name__ == "__main__":    
  url = "https://picsum.photos/2000/3000"
  l1 = [url for i in range(10)]
  l2 = [i for i in range(10)]
  with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(DownloadFile,l1,l2)
    for r in results:
      print(r)