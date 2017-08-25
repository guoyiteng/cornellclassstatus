import requests
from bs4 import BeautifulSoup

def getHTML(url):
	r = requests.get(url)
	return r.text

# for test purpose
def getLocalHTML():
	with open("a.html") as f:
		content = f.read()
		return content

def parseHTML(html):
	soup = BeautifulSoup(html, "html.parser")
	sectionList = []
	for section in soup.find_all(attrs = {"class" : "section"}):
		result = section.get("aria-label")
		if result != None:
			sectionList.append(result)
	statusList = []
	for status in soup.find_all("i"):
		statusList.append(status["class"][2])
	resultDict = {}
	for idx, section in enumerate(sectionList):
		resultDict[section] = statusList[idx]
	return resultDict

def main():
	print("start")
	url = "https://classes.cornell.edu/browse/roster/FA17/class/CS/4820"
	html = getHTML(url)
	print(parseHTML(html))
	return 0

if __name__ == '__main__':
	main()