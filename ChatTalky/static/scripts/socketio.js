/*$(document).ready(function () {
    var socket = io.connect('http://127.0.0.1:5000');
    socket.on('connect', function () {
        socket.send('User is BITE');
        console.log('Nick ta pute');
    });


    socket.on('message', function (msg) {
        $("#mess").append('<li>' + msg + '</li>');
        console.log('Received message');
    });


    $('#sendbutton').on('click', function () {
        socket.send($('#myMessage').val());
        $('#myMessage').val('');
    });
});*/




document.addEventListener('DOMContentLoaded', () => {
/*var socket = io.connect('http://' + document.domain + ':' + location.port);*/
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    let room = 'Room1';

    joinRoom("Room1");





    socket.on('message', data => {
        const p = document.createElement('p');
        const span_username = document.createElement('span');
        const span_timestamp = document.createElement('span');
        const br = document.createElement('br');
        const koko = document.createElement('span');
        var koko2 = document.createElement('span');
        span_username.style.color = "Red";
        span_timestamp.style.color = "Black";
        span_timestamp.style.fontSize = "15px";
        span_username.style.fontSize = "25px";


        if (data.username) {
            span_username.innerHTML = data.username;
            koko.innerHTML = data.msg;
            span_timestamp.innerHTML = data.time_stamp;
            p.innerHTML = span_username.outerHTML + br.outerHTML + koko.outerHTML + br.outerHTML + span_timestamp.outerHTML;
            p.style.border = "none";
            p.style.paddingTop = "13px";
            p.style.paddingLeft = "20px";
            p.style.paddingRight = "20px";
            p.style.paddingBottom = "15px";
            p.style.backgroundColor = "#d4a2d6";
            p.style.width = "100px";
            p.style.borderRadius = "40px"
            document.querySelector('#message-display').append(p);
        }

        
        else {
            printSysMsg(data.msg);
            document.querySelector('#message-display').append(koko2);
        }
    });

    document.querySelector('#send-button').onclick = () => {
        socket.send({ 'msg': document.querySelector('#user_message').value, 'username': username, 'room': room });
        document.querySelector("#user_message").value = '';
    };

    document.querySelectorAll('.select-room').forEach(p => {
        p.onclick = () => {
            let newRoom = p.innerHTML;
            if (newRoom == room) {
                msg = `You are already in ${room}`
                printSysMsg(msg);
            }
            else {
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }
        }
    });

    function leaveRoom(room) {
        socket.emit('leave', { 'username': username, 'room': room });
    }

    function joinRoom(room) {
        socket.emit('join', {'username': username, 'room': room });
        document.querySelector('#message-display').innerHTML = '';
        document.querySelector("#user_message").focus();
    }
    
    function printSysMsg(msg) {
        const p = document.createElement('p');
        p.innerHTML = msg;
        document.querySelector('#message-display').append(p);

    };



});













document.addEventListener('DOMContentLoaded', () => {

    let msg = document.querySelector('#user_message')
    msg.addEventListener('keyup', event => {
        event.preventDefault();
        if (event.keyCode === 13) {
            document.querySelector('#send-button').click();
        }
    })
})