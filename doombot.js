const Discord = require("discord.js")
const config = require("./config.json")
const bot = new Discord.Client();

bot.commands = new Discord.Collection();


bot.on("ready", () => {
  console.log(bot.user.username + " is online.")
});

bot.on("message", async message => {
  //a little bit of data parsing/general checks
 
  if(message.author.bot) return;
  if(message.channel.type === 'dm') return;
  let content = message.content.split(" ");
  let command = content[0];
  let args = content.slice(1);
  let prefix = config.prefix;
  if(!message.content.startsWith(prefix)) return;


bot.login(process.env.BOT_TOKEN);
