import heapq
from collections import Counter

def huffman_codes(text):
    if not text:
        return {}
    heap = [[freq, i, char] for i, (char, freq) in enumerate(Counter(text).items())]
    heapq.heapify(heap)
    serial = len(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, [left[0] + right[0], serial, (left, right)])
        serial += 1

    codes = {}
    def assign(node, code):
        if isinstance(node[2], str):
            codes[node[2]] = code or "0"
        else:
            assign(node[2][0], code + "0")
            assign(node[2][1], code + "1")
    assign(heap[0], "")
    return codes

text = input("Enter text: ")
codes = huffman_codes(text)
print("Huffman codes:")
for char, code in codes.items():
    print(repr(char), ":", code)
