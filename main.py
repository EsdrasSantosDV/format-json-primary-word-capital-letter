import json

def format_text(text):
    if not isinstance(text, str):
        return text
    words = text.split(" ")
    formatted_words = [words[0].capitalize()]
    for word in words[1:]:
        formatted_words.append(word.lower())
    return " ".join(formatted_words)

def format_json(json_data):
    if isinstance(json_data, dict):
        formatted_data = {}
        for key, value in json_data.items():
            formatted_data[key] = format_json(value)
        return formatted_data
    elif isinstance(json_data, list):
        return [format_json(element) for element in json_data]
    else:
        return format_text(json_data)

def main():
    with open('br.json', 'r', encoding='utf-8') as infile:
        json_data = json.load(infile)
    formatted_json = format_json(json_data)
    with open('output.json', 'w', encoding='utf-8') as outfile:
        json.dump(formatted_json, outfile, ensure_ascii=False, indent=4)

main()