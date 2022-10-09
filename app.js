function _all(q, e=document){return e.querySelectorAll(q)}
function _one(q, e=document){return e.querySelector(q)}


async function postTweet() {
    const form = event.target
    //FETCH BTN, set data-await
    console.log("yesyesyes")
    const connection = await fetch("/post_tweet", {
        method: "POST",
        body: new FormData(form)
    })
    console.log("Yaaaassss bitch")
    if (!connection.ok)
    {
        return
    }

    console.log(await connection);
    const connection_text = await connection.text(); //TWEET ID

    const tweet_object = JSON.parse(connection_text);
    
    console.log(tweet_object);
    
    let tweet = ''

    if (tweet_object.tweet.image ) {
    tweet = `
    <section class="tweet" id="${tweet_object.tweet.id}">

    <article>
    <div class="">${tweet_object.tweet.iat}</div>
    <div class="">${tweet_object.tweet.user_firstname}</div>
    <div class="">${tweet_object.tweet.user_lastname}</div>
    <p class="">${tweet_object.tweet.text}</p>
    <img src="/images/${tweet_object.tweet.image}" alt="">

    <div class="">
    <i onclick="delete_tweet('${tweet_object.tweet.id}')" class="fas fa-trash ml-auto"></i>
    <i class="fa-solid fa-message"></i>
    <i class="fa-solid fa-heart"></i>
    <i class="fa-solid fa-retweet"></i>
    <i class="fa-solid fa-share-nodes"></i>
</div>
    <button onclick="delete_tweet('${tweet_object.tweet.id}')">🗑️</button>
    <button onclick="open_modal('${tweet_object.tweet.text}' ,'${tweet_object.tweet.id}', 'true' , '/images/${tweet_object.tweet.image}')">✏️</button>
    
    </article>

</section>
        `
        _one("input", form).value = ""  
    _one("#tweets").insertAdjacentHTML("afterbegin", tweet)
    } else {

        tweet = `
        <section class="tweet" id="${tweet_object.tweet.id}">

        <article>
        <div class="">${tweet_object.tweet.iat}</div>
        <div class="">${tweet_object.tweet.user_firstname}</div>
        <div class="">${tweet_object.tweet.user_lastname}</div>
        <p class="">${tweet_object.tweet.text}</p>
        <div class="">
        <i onclick="delete_tweet('${tweet_object.tweet.id}')" class="fas fa-trash ml-auto"></i>
        <i class="fa-solid fa-message"></i>
        <i class="fa-solid fa-heart"></i>
        <i class="fa-solid fa-retweet"></i>
        <i class="fa-solid fa-share-nodes"></i>
    </div>
        <button onclick="delete_tweet('${tweet_object.tweet.id}')">🗑️</button>
        <button onclick="open_modal('${tweet_object.tweet.text}' ,'${tweet_object.tweet.id}', 'false' )">✏️</button>
        
        </article>

    </section>
    `
    _one("input", form).value = ""  
    _one("#tweets").insertAdjacentHTML("afterbegin", tweet)

}
}

async function delete_tweet(tweet_id){
    console.log(tweet_id)        
    // Connect to the api and delete it from the "database"
        const connection = await fetch(`/delete/${tweet_id}`, {
        method : "DELETE"
        })
        if( ! connection.ok ){
        alert("It didn't work. Try again")
        return
        }
    
        document.querySelector(`[id='${tweet_id}']`).remove()
    }

function open_modal(tweet_text, tweet_id , is_image , imagePath) {
console.log(tweet_text, tweet_id , is_image , imagePath);

//updating image 

if(is_image === "true") {

    document.querySelector("input[type=text]").value = tweet_id;
    document.querySelector(".modal_container").style.display = "block";
    document.getElementById("update_text").value = tweet_text;
    document.querySelector(".cancelBTN").addEventListener("click", closeModal);

    document.querySelector("#updated_image").setAttribute("src", imagePath);

} else if (is_image === "false") {
    document.querySelector("#image_update_container").style.display = "none";

}

document.querySelector("input[type=text]").value = tweet_id;
document.querySelector(".modal_container").style.display = "block";
document.getElementById("update_text").value = tweet_text;
document.querySelector(".cancelBTN").addEventListener("click", closeModal);

}

function closeModal() {
    document.querySelector(".modal_container").style.display = "none";

}

async function updateTweet() {
    console.log("hahahahaha")

    const form = event.target
    //FETCH BTN, set data-await
    console.log("yesyesyes")
    const connection = await fetch("/update", {
        method: "PUT",
        body: new FormData(form)
    })

    if (!connection.ok) {
        return
    }

    const connection_text = await connection.text(); //TWEET ID
    const tweet_object = JSON.parse(connection_text);
    
    _one("#tweets").innerHTML = "";
    tweet_object.tweets.forEach(tweet => {
        if (tweet_object.user_id == tweet.user_id) {
            const updated_tweet = 
            `
            <section class="tweet" id="${tweet.id}">

            <article>
            <div class="">${tweet.iat}</div>
            <div class="">${tweet.user_firstname}</div>
            <div class="">${tweet.user_lastname}</div>
            <p class="">${tweet.text}</p>
            <div class="">
            <i onclick="delete_tweet('${tweet.id}')" class="fas fa-trash ml-auto"></i>
            <i class="fa-solid fa-message"></i>
            <i class="fa-solid fa-heart"></i>
            <i class="fa-solid fa-retweet"></i>
            <i class="fa-solid fa-share-nodes"></i>
        </div>
            <button onclick="delete_tweet('${tweet.id}')">🗑️</button>
            <button onclick="open_modal('${tweet.id}','false' ,'${tweet.text}')">✏️</button>
            
            </article>
    
        </section>
        `

        _one("#tweets").insertAdjacentHTML("afterbegin", updated_tweet);
        _one(".modal_container").style.display = "none";

        }
    });
}

// FOLLOW FUNCTION 

async function follow_user() {
    const form = event.target
    //FETCH BTN, set data-await
    console.log("yesyesyes")
    const connection = await fetch("/follow", {
        method: "POST",
        body: new FormData(form)
    })
    console.log("Yaaaassss bitch")
    if (!connection.ok)
    {
        return
    }

    console.log(await connection);
    const connection_text = await connection.text(); //TWEET ID
    console.log(connection_text);
}

// EMAIL 

async function sendEMAIL() {
    const form = event.target
    //FETCH BTN, set data-await
    console.log("Let's see")
    const connection = await fetch("/signUp", {
        method: "POST",
        body: new FormData(form)
    })
    console.log("It's goods")
    if (!connection.ok)
    {
        return
    }

    console.log(await connection);
    const connection_text = await connection.text(); //TWEET ID
    console.log(connection_text);
}