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
    // const tweet_id = connection_text.slice(0, 36);
    // const tweet_image = connection_text.slice(26, 40);
    // const tweet_iat = connection_text.slice(40)
    // console.log(connection_text, tweet_id, tweet_image, tweet_iat);

    //const image_path = _one("input[type=file]", form).value.replaceAll(" ", "-").trim()
    
    let tweet = ''

    if (tweet_object.tweet_image == "true") {
    tweet = `
        <section class="tweet" id="${tweet_object.tweet.id}">
            <p class="tweet_time">${tweet_object.tweet.iat}</p>
            <p class="">yes i am</p>
            <article >
            <button onclick="openModuleUpdate('${tweet_object.tweet.id}','true' ,'' , '/image/${image_path.substring(image_path.lastIndexOf("\\") + 1)}')">✏️</button>
            </article>
            <img src="/image/${image_path.substring(image_path.lastIndexOf("\\") + 1)}" alt="">
        </section>
        `
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
        <button onclick="openModuleUpdate('${tweet_object.tweet.id}','false' ,'${tweet_object.tweet.text}')">✏️</button>
        
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
    


