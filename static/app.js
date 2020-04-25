var homeTeam = prompt("Who Is The Home Team?");
var awayTeam = prompt("Who Is The Away Team?");
var sponsorName = prompt("Who Is Sponsoring This Game?");

document.write("The Home Hockey Team Is: " + homeTeam);
document.write("<br>");
document.write("The Away Hockey Team Is: " + awayTeam);
document.write("<br>");

console.log('Todays Game Brought To You By ' + sponsorName + " is between " + homeTeam + " and " + awayTeam);

if (homeTeam.length > awayTeam.length){
  console.log("The Home Team Has A Longer Name!");
} if (homeTeam.length < awayTeam.length){
  console.log("The Away Team Has A Longer Name!");
} if (homeTeam.length === awayTeam.length){
  console.log("Their Team Name Length Is Equal!");
}

var homeTeamGoals = prompt("How Many Goals Has " + homeTeam + " scored?");
var awayTeamGoals = prompt("How Many Goals Has " + awayTeam + " scored?");

console.log("Looks like " + homeTeam + " has scored " + homeTeamGoals + " goals, while " + awayTeam + " has scored " + awayTeamGoals + " goals.");

if (homeTeamGoals > awayTeamGoals){
  document.write("<br>");
  document.write("Looks like " + homeTeam + " is winning!");
} if (homeTeamGoals < awayTeamGoals){
  document.write("<br>");
  document.write("Looks like " + awayTeam + " is winning!");
} if (homeTeamGoals === awayTeamGoals){
  document.write("<br>");
  document.write("We got ourselves a tie game!");
}
