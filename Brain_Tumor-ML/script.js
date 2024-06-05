function displayImage(event) {
    const uploadedImage = document.getElementById('uploadedImage');
    uploadedImage.src = URL.createObjectURL(event.target.files[0]);
    uploadedImage.style.display = 'block';
}

function uploadImage() {
    const form = document.getElementById('imageInput');
    const file = imageInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        const resultText = document.getElementById('resultText');

        resultText.innerHTML = '';

        fetch('http://127.0.0.1:8000/upload', { // Replace 'your-backend-endpoint' with your actual backend URL
            method: 'POST',
            body: formData
        })

        .then(response => response.json())
        .then(data => {
            const result = data.result; // Assuming the result is in data.result
            resultText.innerHTML = `<b>RESULT : </b> <span style="color:black">${result}</span>`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultText.innerHTML = 'Error processing the image.';
        });  
    };
}
