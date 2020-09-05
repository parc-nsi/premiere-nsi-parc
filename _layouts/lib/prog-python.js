/* Source pro_python.js de JM Meny pour Python_UPO */
/*Nécessite Jquery, Skulpt et CodeMirror  */

$(function(){

/*Paramétrage de Skulpt*/
// output functions are configurable.  This one just appends some text
// to a pre element.
function outf(i, text) { 
    var mypre = document.getElementById("sortie_python" + i); 
    mypre.innerHTML = mypre.innerHTML + text; 
} 
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}
// Here's everything you need to run a python program in skulpt
// grab the code from your textarea
// get a reference to your pre element for output
// configure the output function
// call Sk.importMainWithBody()
    
function runit(i) { 
   var prog = editeurs[i].getValue(); 
   var mypre = document.getElementById("sortie_python" + i); 
   mypre.innerHTML = ''; 
   Sk.pre = "sortie_python" + i;
   Sk.configure({output:function(text){outf(i, text)}, read:builtinRead, python3:true}); 
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = "tortue" + i;
   var myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, prog, true);
   });
   myPromise.then(function(mod) {
       console.log('success');
   },
       function(err) {
       console.log(err.toString());
   });
} 
    
/* Récupération des éléments HTML par l'API DOM */
var codes = document.querySelectorAll(".code_python");
var sorties = document.querySelectorAll(".sortie_python");
var boutons = document.querySelectorAll(".execution");
var canevas = document.querySelectorAll(".tortue");
var editeurs = [];
    
/* Ajout d'identifiants aux éléments HTML */
for(let i=0; i < codes.length; i++){
		codes[i].setAttribute("id","code_python" + i);
		}

for(let i=0; i < sorties.length; i++){
		sorties[i].setAttribute("id","sortie_python" + i);
		}

for(let i=0; i < canevas.length; i++){
		canevas[i].setAttribute("id","tortue" + i);
		}
    
    
for(let i=0; i < codes.length; i++){
    editeurs[i] = CodeMirror.fromTextArea(codes[i], {lineNumbers: true, mode: "python" });
}
    
/*  Ajout d'écouteurs d'événements sur les boutons */
    
for(let i=0; i < boutons.length; i++){
    boutons[i].addEventListener("click", function(){runit(i)});
}
    
}
)
