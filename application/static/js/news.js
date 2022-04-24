function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function send(socket) {
    await sleep(1000);
    socket.send('send_news');
}

let socket = new WebSocket('ws://127.0.0.1:8000/ws/news/');

window.client_data = {
    data: []
};

socket.onmessage = function(event) {
    let server_data = JSON.parse(event.data);
    let status = server_data.status;

    if (status === 'connected') {
        console.log('Websocket connected');
        socket.send('send_news');

    } else if (status === 'data_news') {
        console.log('Data news!');
        let news_list = server_data.values;
        if (!(news_list.length === client_data.data.length)) {
            let block = document.querySelector('#test_block');
            let index;
            for (index = 0; index < news_list.length; ++index) {
                let news = news_list[index];
                /*
                news - object: [name, category, ...]
                news_block: document element
                */
                let li = document.createElement('li');
                let div1 = document.createElement('div');
                div1.classList = ["row our_cells our_main_divs"];
                let div2 = document.createElement('div');
                div2.classList = ["row"];
                div2.style['display'] = 'flex';
                div2.style['justify-content'] = 'center';
                div2.style['font-size'] = '2rem';
                div2.innerText = news.name;
                let div3 = document.createElement('div');
                div3.classList = ["row"];
                div3.style['margin-top'] = '5px';
                let div4 = document.createElement('div');
                div4.classList = ["col-8"];
                let div5 = document.createElement('div');
                div5.classList = ['news_menu'];
                div5.style['font-size'] = '1rem';
                div5.innerText = news.short_text;
                let div6 = document.createElement('div');
                div6.classList = ["col-4"];
                let div7 = document.createElement('div');
                div7.style['font-size'] = '1rem';
                div7.innerText = 'Дата публикации: ' + news.date;
                let div8 = document.createElement('div');
                div8.style['font-size'] = '1rem';
                div8.innerText = 'Источник: ' + news.source;
                let div9 = document.createElement('div');
                div9.style['font-size'] = '1rem';
                div9.innerText = 'Категория: ' + news.category;

                div6.appendChild(div7);
                div6.appendChild(div8);
                div6.appendChild(div9);

                div4.appendChild(div5);

                div3.appendChild(div4);
                div3.appendChild(div6);

                div1.appendChild(div2);
                div1.appendChild(div3);
                li.style['margin-top'] = '5px';
                li.appendChild(div1);
                block.appendChild(li);

            }
            window.client_data.data = news_list;
        }
        send(socket);
        
    } else {
        console.log('garbage');
    }
}


socket.onopen = function() {
    console.log('Onopen');
}

socket.onclose = function(event) {
    console.log('Onclose');
}

socket.onerror = function(error) {
    console.log('Ошибка ' + error.message);
}