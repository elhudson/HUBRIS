
const tiers = document.getElementsByName("tier");
const ability_scores = document.getElementsByClassName("ability_score");
const skills=document.getElementsByClassName("skill_bonus");
const proficiencies=document.getElementsByClassName("is_proficient");
const stats=readStats();




function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
} 

function readStats() {
  var stats=new Object();
  stats.str=document.getElementById("str").value,
  stats.dex=document.getElementById("dex").value,
  /* stats.con=document.getElementById("con").value,
  stats.int=document.getElementById("int").value,
  stats.wis=document.getElementById("wis").value,
  stats.cha=document.getElementById("cha").value, */
  stats.pb=document.getElementById("proficiency_bonus").innerHTML;
  stats.tier=document.querySelector('input[name="tier"]:checked').value; 
  return stats;
}

function setProficiency() {
  for (var i = 0; i < tiers.length; i++) {
    if (tiers[i].checked) {
      document.querySelector("#proficiency_bonus").innerHTML =
        Number(tiers[i].value) + 1;
    }
  }
}

function setSkill(checkbox_name, skill_name) {
  var checkbox = document.getElementById(checkbox_name);
  var skill = document.getElementById(skill_name);
  var ability = checkbox.getAttribute("data-stat");
  var ability_score = statMatch(ability);
  if (checkbox.checked) {
    skill.value = Number(stats.pb) + ability_score;
  }
  else {
    skill.value = ability_score;
  }
}

function statMatch(ability_score) {
  let stat = document.querySelector("#" + ability_score).value;
  return Number(stat);
}

function populateAbilities() {
  for (i = 0; i < skills; i++) {
    skill_name=skills[i].id;
    skill_checked=proficiencies[i].id;
    setSkill(skill_checked,skill_name);
  }
}