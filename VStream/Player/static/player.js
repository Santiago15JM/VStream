function changeSource(fileName) {
  player = document.getElementById("player");
  player.setAttribute("src", `../static/videos/${fileName}`);
  console.log(fileName);
}
