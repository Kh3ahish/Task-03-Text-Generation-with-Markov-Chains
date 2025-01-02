function buildMarkovChain(text, n) {
    const words = text.split(/\s+/);
    const chain = {};

    for (let i = 0; i <= words.length - n; i++) {
        const key = words.slice(i, i + n).join(' ');
        const nextWord = words[i + n];

        if (!chain[key]) {
            chain[key] = [];
        }
        if (nextWord) {
            chain[key].push(nextWord);
        }
    }

    return chain;
}

function generateText() {
    const dataset = document.getElementById('dataset').value;
    const ngram = parseInt(document.getElementById('ngram').value);
    const length = parseInt(document.getElementById('length').value);

    if (!dataset || !ngram || !length) {
        alert('Please fill in all fields.');
        return;
    }

    const chain = buildMarkovChain(dataset, ngram);
    const keys = Object.keys(chain);

    if (keys.length === 0) {
        alert('Insufficient data for the chosen n-gram size.');
        return;
    }

    let key = keys[Math.floor(Math.random() * keys.length)];
    const result = key.split(' ');

    for (let i = 0; i < length - ngram; i++) {
        const nextWords = chain[key];

        if (!nextWords || nextWords.length === 0) {
            break;
        }

        const nextWord = nextWords[Math.floor(Math.random() * nextWords.length)];
        result.push(nextWord);

        key = result.slice(result.length - ngram).join(' ');
    }

    document.getElementById('generatedText').innerText = result.join(' ');
    document.getElementById('output').style.display = 'block';
}
