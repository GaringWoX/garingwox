const Discord = require('discord.js');

const client = new Discord.Client();

 

client.on('ready', () => {
    client.setActivity('Take The Pill & Chill', { type: 'WATCHING'})
});


client.on('message', message => {

    if (message.content === 'ping') {

       message.reply('pong');

       }

});

 


client.login(process.env.BOT_TOKEN);
