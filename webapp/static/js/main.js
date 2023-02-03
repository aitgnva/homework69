async function makeRequest(url, method) {
    let response = await fetch(url, method);
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        return await response.json();
    }
}

function getToken(name){
    let cookie = {}
    document.cookie.split(';').forEach(function (el){
        let [key, value] = el.split('=');
        cookie[key.trim()] = value
    })
    return cookie[name]
}

async function buttonClick(event) {
    let target = event.target;
    let url = target.dataset['url'];
    let data = {
        "a": document.getElementById('a').value,
        "b": document.getElementById('b').value
    };

    console.log(data)
    let csrftoken = getToken("csrftoken");

    let response = await makeRequest(url, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
    let answer = document.getElementById('answer');
    answer.innerText = `Answer: ${response.answer}`
    console.log(response)

}

