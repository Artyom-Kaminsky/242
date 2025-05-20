let csrf_token = document.cookie.split("=")[1];

function likePost(postId){
    fetch(`${postId}/like`, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
    }).then(response => response.json())
    .then(data => {
        document.getElementById("likeButton").innerText = `👍${data.likes}`;
    });
}

function dislikePost(postId){
    fetch(`${postId}/dislike`, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
    }).then(response => response.json())
    .then(data => {
        document.getElementById("dislikeButton").innerText = `👎${data.dislikes}`;
    });
}