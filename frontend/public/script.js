async function countWords() {
    const textArea = document.getElementById('text');
    const resultElement = document.getElementById('result');
    const errorElement = document.getElementById('error');

    const textToCount = textArea.value;

    try {
        const response = await fetch('http://localhost:8000/words/count', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: textToCount }),
        });

        const data = await response.json();

        if (response.ok) {
            resultElement.textContent = `Word Count: ${data.word_count}`;
            errorElement.textContent = '';
        } else {
            errorElement.textContent = '';

            data.detail.forEach(element => {
                errorElement.textContent += `${element.msg} \n`;
            });
            resultElement.textContent = '';
        }
    } catch (error) {
        errorElement.textContent = 'An error occurred while counting words.';
        resultElement.textContent = '';
    }
}
