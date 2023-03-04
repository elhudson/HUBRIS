
const tiers = document.getElementsByName("tier");
const ability_scores = document.getElementsByClassName("ability_score");
const skill_bonuses=document.getElementsByClassName("skill_bonus");
const skill_profs=document.getElementsByClassName("is_proficient");

function start(align,tier,hit_die,skills) {
  setAlignment(align)
  setTier(tier)
  setProficiency()
  setHD(hit_die)
  populateProficiencies(skills)
  populateModifiers()
  
}

function populateProficiencies(proficiencies) {
  ps=proficiencies.split(",")
  for (var i=0;i<(ps.length);i++) {
    prof=ps[i]
    for (var j=0;j<skill_profs.length;j++) {
      skill=skill_profs[j]
      s=skill.getAttribute("id")
      if (prof==s) {
        skill.setAttribute("checked",true)
      } 
  }
}
}

function populateModifiers() {
  for (var i=0;i<skill_bonuses.length;i++) {
    console.log(skill_bonuses[i].getAttribute("name"))
    attr=skill_bonuses[i].getAttribute("data-stat")
    attr_value=statMatch(attr)
    is_prof=skill_profs[i].checked
    console.log(is_prof)
    pb=Number(document.getElementById("proficiency_bonus").innerHTML)
    console.log(pb)
    if (is_prof==true) {
      bonus=pb+attr_value
    }
    else {
      bonus=attr_value
    }
    skill_bonuses[i].setAttribute("value",bonus)
  }
}

function setAlignment(align) {

        const menu=document.getElementById("alignment");
        const options=menu.options;
                for(var i=0; i<options.length; i++){ 
                  if (options[i].value===align) {
                    print(options[i])
                    options[i].setAttribute("selected",true)
                  }
                }
              }

function setHD(hit_die) {
  const ch=document.getElementById(hit_die)
  ch.setAttribute("checked",true)
}

function setTier(tier) {
  if (Number(tier)==1) {
    document.getElementById("tier_1").setAttribute("checked",true)
  }
  if (Number(tier)==2) {
    document.getElementById("tier_2").setAttribute("checked",true)
  }
  if (tier==3) {
    document.getElementById("tier_3").setAttribute("checked",true)
  }
  if (tier==4) {
    document.getElementById("tier_4").setAttribute("checked",true)
  }
}

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

function setProficiency() {
  for (var i = 0; i < tiers.length; i++) {
    if (tiers[i].checked) {
      document.querySelector("#proficiency_bonus").innerHTML =
        Number(tiers[i].value) + 1;
    }
  }
}


function statMatch(ability_score) {
  let stat = document.getElementById(ability_score).innerHTML;
  return Number(stat);
}
