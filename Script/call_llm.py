import requests
import json
import os
from google import genai
from google.genai import types

OLLAMA_ENDPOINT = os.environ.get("OLLAMA_ENDPOINT", "http://localhost:11434/api/generate")
OLLAMA_MODEL_NAME = os.environ.get("OLLAMA_MODEL_NAME", "gemma3:12b")
GEMINI_MODEL_NAME = os.environ.get("GEMINI_MODEL_NAME", "gemini-2.5-flash")


def generate_prompt(title,content,tags):
    prompt = f"""
You are given a LeetCode problem:

Title:
{title}

Code:
{content}

From the list of tags:
{tags}

Identify all relevant tags that describe this problem based on the code.
Use ONLY the tags provided, and do not invent new tags.

Respond ONLY with a JSON array like ["array", "greedy"]. 
Do NOT add anything else — no explanations, no formatting, no code block fences like ```.

Just output the plain JSON list on a single line.
"""
    return prompt


def call_ollama(title, content, tags):
    
    prompt = generate_prompt(title, content, tags)

    response = requests.post(
        OLLAMA_ENDPOINT,
        headers={"Content-Type": "application/json"},
        json={"model": OLLAMA_MODEL_NAME, "prompt": prompt, "stream": False},
    )

    result = response.json()
    try:
        return json.loads(result["response"].strip())
    except:
        print(f"Failed to parse response: {result['response']}")
        return []

def call_gemini(title, content, tags):
    client = genai.Client()
    response = client.models.generate_content(
        model = GEMINI_MODEL_NAME,
        contents = generate_prompt(title, content, tags),
        config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)
)
    )
    try:
        return json.loads(response.text.strip())
    except:
        print(f"Failed to parse Gemini response: {response.text}")
        return []


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    title = "23. Merge k Sorted Lists"
    content = """
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode()
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
"""

    tags = [
        "array", "linked list", "heap", "greedy", "divide and conquer",
        "dynamic programming", "binary search", "stack", "recursion", "hash table"
    ]

    selected_tags = call_gemini(title, content, tags)
    print("Selected tags:", selected_tags)

    expected_tags = {"linked list", "heap", "greedy"}
    print("✅ Correct tags present?", expected_tags.issubset(set(selected_tags)))

