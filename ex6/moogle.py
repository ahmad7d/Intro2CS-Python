import pickle
import sys
from bs4 import BeautifulSoup
import requests
import urllib.parse


def read_links(filename):
    links_lst = []
    with open(filename, 'r') as file:
        for link in file:
            links_lst += link.strip().split()
        file.close()
    return links_lst


def request(web):
    response = requests.get(web)
    return response.text


def searching(html):
    lst = []
    soup = BeautifulSoup(html, 'html.parser')
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            if target:
                lst.append(target)
    return lst


def counting_links(links_lst):
    d = {}
    for link in links_lst:
        d[link] = links_lst.count(link)
    return d


def merge(web, index_file):
    return urllib.parse.urljoin(web, index_file)


def creating_d(web, inp_file):
    d = {}
    links_lst = read_links(inp_file)
    for link in links_lst:
        d[link] = counting_links(searching(request(merge(web, link))))
    return d


def saving_d(filename, d):
    with open(filename, 'wb') as f:
        pickle.dump(d, f)


def main_1(web, inp_file, outp_file):
    d = creating_d(web, inp_file)
    saving_d(outp_file, d)


# print(main_1("https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/", "small_index.txt", "agagaga"))
# "https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/", "small_index.txt"
#######################################################################################################################
def importing_the_d(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def sum_d(d):
    values = d.values()
    return sum(values)


def page_rank_process(n, d, r):
    while n > 0:
        for i in d:
            for j in d[i]:
                r[j][1] = d[i][j] * r[j][0] / sum_d(d[i])
        for k in r:
            r[k][0], r[k][1] = r[k][1], 0
        n -= 1
    return r


# def getting_links_lst(file):
#     links_lst = []
#     links_file = importing_the_d(file)
#     for link in links_file:
#         links_lst.append(link)
#     return links_lst


def sorting_web(n, d):
    r = {}
    for link in d:
        r[link] = [1.0, 0]
    new_r = page_rank_process(n, d, r)
    for i in new_r:
        new_r[i] = new_r[i][0]
    return new_r


def main_2(iterations, dict_filename, outp_filename):
    iterations = int(iterations)
    d = importing_the_d(dict_filename)
    new_d = sorting_web(iterations, d)
    saving_d(outp_filename, new_d)


# print(sorting_web(60, "https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/", "small_index.txt"))
#######################################################################################################################


def word_searching(html):
    words_lst = []
    soup = BeautifulSoup(html, 'html.parser')
    for p in soup.find_all("p"):
        words_lst.append(p.text.strip().split())
    return words_lst


def words_counter(words_lst):
    d = {}
    for i in words_lst:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    return d


def update_page_words_occ(words_d, link, words_count):
    for word in words_count:
        if word not in words_d:
            words_d[word] = {}
        words_d[word][link] = words_count[word]


def main_search(base_url, index_file):
    links_list = read_links(index_file)
    words_d = {}
    for link in links_list:
        words_count = words_counter(word_searching(request(merge(base_url, link))))
        update_page_words_occ(words_d, link, words_count)
    return words_d


def main_3(base_url, index_file, outp_file):
    new_d = main_search(base_url, index_file)
    saving_d(outp_file, new_d)


# print(main_3("https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/", "small_index.txt", 'as'))
#######################################################################################################################


def list_includes(lst1, lst2):
    return set(lst2) <= set(lst1)


def calculate_weight(query, words_d, page, page_rank):
    count = 0
    while True:
        for word in query:
            if words_d[word][page] <= 0:
                return count * page_rank
            words_d[word][page] -= 1
        count += 1


def print_pages_weight(pages_weight):
    for page, weight in pages_weight:
        print(page, weight)


def main_4(query, ranking_file, words_file, max_results):
    max_results = int(max_results)
    ranking_d = importing_the_d(ranking_file)
    words_d = importing_the_d(words_file)
    query = [word for word in query.split(' ') if word in words_d]
    if len(query) == 0:
        return
    desired_pages = set(words_d[query[0]].keys())
    # print(query)
    for word in query[1:]:
        desired_pages = desired_pages.intersection(set(words_d[word].keys()))
    desired_pages = sorted(desired_pages, key=lambda p: ranking_d[p], reverse=True)[:max_results]
    pages_weight = sorted([(page, calculate_weight(query, words_d, page, ranking_d[page]))
                           for page in desired_pages],
                          key=lambda p: p[1], reverse=True)
    print_pages_weight(pages_weight)


if __name__ == '__main__':
    if len(sys.argv) not in [5, 6]:
        print('invalid number')
    elif sys.argv[1] == 'crawl':
        main_1(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == 'page_rank':
        main_2(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == 'words_dict':
        main_3(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == 'search':
        main_4(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

# def separate_links():
#     outp_file = {}
