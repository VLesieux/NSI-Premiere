var itemCounter = 0;
var liveCounter = 3;

var mySprite_col;
var mySprite_row;
var decor;
var item={};
var t0,t1;
var background = [

[95,95,95,95,95,124,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,124,95,95,95,95,95],
[124,95,95,95,124,124,124,95,124,124,124,124,124,124,95,124,124,124,124,124,124,124,124,124,124,95,124,95,95,124,124,95],
[124,95,124,95,95,95,95,95,95,124,95,95,95,95,95,124,95,95,95,95,95,95,95,124,95,95,124,124,95,95,95,95],
[124,95,124,124,95,124,95,95,95,124,95,124,124,124,124,124,95,124,124,124,124,124,124,124,95,95,95,124,124,124,124,95],
[95,95,124,124,95,124,124,124,124,124,95,95,95,95,95,124,95,95,95,95,124,95,95,124,95,95,95,124,95,95,95,95],
[124,124,124,95,95,95,95,95,95,124,124,124,124,95,95,95,95,95,124,95,124,95,95,95,95,124,124,124,95,95,124,95],
[95,95,124,95,124,95,95,95,95,95,95,95,124,124,124,124,124,95,124,124,124,95,124,95,95,95,95,95,95,124,124,95],
[95,95,95,95,124,95,95,124,124,95,95,95,95,95,95,95,124,95,95,95,95,95,124,95,95,124,95,95,124,95,95,95],
[95,95,95,124,124,95,95,95,124,124,124,124,124,124,124,124,124,124,124,124,95,95,95,95,95,124,95,95,124,95,95,95],
[95,95,95,95,124,124,124,95,124,95,95,95,95,95,95,95,95,95,95,124,95,124,124,124,95,124,124,124,124,124,124,95],
[95,124,95,95,95,95,124,124,124,95,95,95,124,95,95,124,95,124,95,124,95,124,124,95,95,95,95,124,95,95,95,95],
[124,124,95,124,95,95,124,95,124,95,124,124,124,95,124,124,95,124,124,124,95,124,124,95,95,124,124,124,95,95,95,95],
[95,95,95,124,95,95,124,95,95,95,124,95,95,95,95,124,95,95,95,95,95,95,124,124,95,95,124,95,95,124,124,95],
[95,124,95,95,95,95,124,95,124,124,124,95,124,124,124,124,124,124,124,124,95,95,95,95,95,95,124,95,95,124,95,95],
[95,124,95,124,95,95,95,95,95,95,124,95,124,95,95,95,95,124,95,95,95,95,124,124,95,124,124,95,95,124,95,95],
[95,124,95,124,95,124,124,124,95,95,124,95,95,95,95,95,95,124,124,124,124,124,124,95,95,95,124,95,95,124,95,95],
[95,124,95,124,95,95,124,95,95,124,124,124,124,124,124,124,124,124,95,95,95,95,124,95,95,95,124,124,124,124,95,95],
[124,124,95,124,124,95,124,95,95,95,95,95,124,95,95,95,95,124,95,124,95,95,124,95,95,95,124,95,95,95,95,95],
[95,95,95,95,124,95,95,124,124,124,124,124,124,95,124,95,95,95,95,124,124,124,124,95,95,124,124,95,95,124,124,95],
[95,95,124,124,124,95,95,95,95,95,95,95,95,95,124,124,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95]

 ];

//le dessin du personnage
var personnagesTiles = new Image();
personnagesTiles.src = 'personnagesTiles.png';
var numero_image_boy=0;
var personnage=[[288,0],[320,0],[352,0],[288,128],[320,128],[352,128]];
var invulnerable=[[0,0],[32,0],[64,0],[0,128],[32,128],[64,128]];
var bientotvulnerable=[[96,0],[128,0],[160,0],[96,128],[128,128],[160,128]];
var argent = new Image();
argent.src='bag.png';

var power = new Image();
power.src='power.png';

//interaction clavier
var keysDown = {};

window.addEventListener('keydown', function(e) {
    keysDown[e.keyCode] = true;
});
window.addEventListener('keyup', function(e) {
    delete keysDown[e.keyCode];
});
//



var bgcanvas = document.getElementById('background');
var bgctx = bgcanvas.getContext('2d');

var spcanvas = document.getElementById('sprite');
var spctx = spcanvas.getContext('2d');




var tilesetImage = new Image();
tilesetImage.src = 'tileset.png';
tilesetImage.onload = drawBackground; //Au chargement de l'image, dessine le background



var bgcanvas = document.getElementById('background');
var bgctx = bgcanvas.getContext('2d');

var spcanvas = document.getElementById('sprite');
var spctx = spcanvas.getContext('2d');

var tileSize = 32;       // La taille d'une dalle (32*32)
var rowTileCount = 20;   // Le nombre de dalles par ligne dans le canvas
var colTileCount = 32;   // Le nombre de dalles par colonne dans le canvas
var imageNumTiles = 16;  // Le nombre de dalles par ligne dans le canvas



function decoration() {

if (mySprite.state==3) {//up
mySprite_row=Math.floor((mySprite.y)/tileSize);
mySprite_col=Math.floor((mySprite.x+mySprite.width/2)/tileSize);
}

if (mySprite.state==2) {//Right
mySprite_row=Math.floor((mySprite.y+mySprite.height/2)/tileSize);
mySprite_col=Math.floor((mySprite.x+mySprite.width)/tileSize);
}

if (mySprite.state==0) {//Down
mySprite_row=Math.floor((mySprite.y+mySprite.height)/tileSize);
mySprite_col=Math.floor((mySprite.x+mySprite.width/2)/tileSize);
}

if (mySprite.state==1) {//Left
mySprite_row=Math.floor((mySprite.y+mySprite.width/2)/tileSize);
mySprite_col=Math.floor((mySprite.x)/tileSize);
}

decor=background [mySprite_row] [mySprite_col];

if (decor!=95 || mySprite.x<4 || mySprite.x>spcanvas.width || mySprite.y<4 || mySprite.y>(spcanvas.height-4-mySprite.height))

{
    return true;
}
}

function init() {

item = {
    x: Math.random() * spcanvas.width,
    y: Math.random() * spcanvas.height,
    width: 10,
    height: 10
};

item_row=Math.floor((item.y+item.width/2)/tileSize);
item_col=Math.floor((item.x+item.height/2)/tileSize);

argent.onload = spctx.drawImage(argent, item.x, item.y);

power.onload = spctx.drawImage(power, 100, 100);

decor=background [item_row] [item_col];

if (decor != 95) {
    init();
}

drawBackground();

mySprite.x=70;
mySprite.y=10;

run();

}

function drawBackground () { 

for (var i=1; i<=rowTileCount; i++) {

for (var j=1; j<=colTileCount; j++) {

var value=background [i-1] [j-1];
var sx=(value%16-1)*32;
var sy=Math.floor(value/16)*32;
var dx=(j-1)*32;
var dy=(i-1)*32;
bgctx.drawImage(tilesetImage,sx,sy,32,32,dx,dy,32,32);

}
}
} 


function update() {

 if (liveCounter==0) {

    bgctx.font = '40pt Arial';
    bgctx.fillStyle = '#ff0000';
    bgctx.textBaseline = 'top';
    bgctx.fillText("Game Over", 350, bgcanvas.height/2);

   
   clearInterval(myTimer);


    } 

   for (var i=0;i<=2;i++) {
ennemis[i].move();
}

    if (37 in keysDown) {
        mySprite.state = 1; //left
        mySprite.x -= 4;
numero_image_boy++;
        if (decoration()) {
        mySprite.x += 4;    
        }
    }

    if (38 in keysDown) {
        mySprite.state = 3; //up
        mySprite.y -= 4;
numero_image_boy++;
        if (decoration()) {
        mySprite.y += 4;  
        }
    }

    if (39 in keysDown) {
        mySprite.state = 2; //right
        mySprite.x += 4;
numero_image_boy++;
        if (decoration()) {
        mySprite.x -= 4;
        }
    }

    if (40 in keysDown) {
        mySprite.state = 0; //down
        mySprite.y += 4;
numero_image_boy++;
        if (decoration()) {
        mySprite.y -= 4;
        }
    }

mySprite.detectCollision();

  if (
        mySprite.x < item.x + item.width &&
        mySprite.x + mySprite.width > item.x &&
        mySprite.y < item.y + item.height &&
        mySprite.y + mySprite.height > item.y
    ) {
        spctx.clearRect(item.x, item.y, item.width, item.height);
        init();
        itemCounter ++;
    }

    if (
        mySprite.x < 820 &&
        mySprite.x + mySprite.width > 800 &&
        mySprite.y < 120 &&
        mySprite.y + mySprite.height > 100
    ) {
        
mySprite.etat="invulnerable";
t0=new Date().getTime();

    }

}

function mySprite(x,y,state,etat) { 

this.width= 32;
this.height= 32;

this.x=x;
this.y=y;

this.state=state;

this.etat=etat;

this.draw=function() {

if (this.etat=="vulnerable") {
    spctx.drawImage(
            personnagesTiles,
            personnage[numero_image_boy][0],
            personnage[numero_image_boy][1] + this.state*32, 
            this.width,
            this.height,
            this.x,
            this.y,
            this.width,
            this.height
        );
}

if (this.etat=="invulnerable") {

t1=new Date().getTime();

if (t1-t0<7000) {

    spctx.drawImage(
            personnagesTiles,
            invulnerable[numero_image_boy][0],
            invulnerable[numero_image_boy][1] + this.state*32, 
            this.width,
            this.height,
            this.x,
            this.y,
            this.width,
            this.height
        );
}

if (t1-t0>7000 && t1-t0<10000) {

  spctx.drawImage(
            personnagesTiles,
            bientotvulnerable[numero_image_boy][0],
            bientotvulnerable[numero_image_boy][1] + this.state*32, 
            this.width,
            this.height,
            this.x,
            this.y,
            this.width,
            this.height
        );



}

if (t1-t0>10000) {this.etat="vulnerable"}

}



};

this.detectCollision=function() {

if (this.etat=="vulnerable") {

for (var i = 0; i <=2; i++) {

if (
        mySprite.x < ennemis[i].x + ennemis[i].width &&
        mySprite.x + mySprite.width > ennemis[i].x &&
        mySprite.y < ennemis[i].y + ennemis[i].height &&
        mySprite.y + mySprite.height > ennemis[i].y
    ) 

{
    liveCounter -=1;
    init();

}

}


}
}

}

var mySprite=new mySprite(70,10,0,"vulnerable");


function render() {

spctx.clearRect(0, 0, spcanvas.width, spcanvas.height);
spctx.font = '12pt Arial';
spctx.fillStyle = '#fff';
spctx.textBaseline = 'top';
spctx.fillText(itemCounter, 10, 10);
spctx.fillText(liveCounter, 990, 10);

spctx.drawImage(argent, item.x, item.y);
spctx.drawImage(power, 800, 100);

for (var i=0;i<=2;i++) {
ennemis[i].draw();
}
    
if (numero_image_boy>=5) {numero_image_boy=0};

mySprite.draw();

   }

function run() {
	update();
	render();
}

var policiers=[[192,0],[224,0],[256,0],[192,128],[224,128],[256,128]];
var positioninpaths=[0,0,0];
var paths=[

[[672,254],[672,164],[770,164],[770,64],[798,64],[798,2],[224,2],[224,64],[132,64],[132,156],[94,156],[94,218],[60,218],[60,324],[164,324],[164,448],[222,448],[222,380],[288,380],[288,294],[516,294],[516,378],[648,378],[648,254],[672,254]],

[[672,254],[638,254],[638,382],[520,382],[520,294],[288,294],[288,374],[226,374],[226,444],[168,444],[168,324],[66,324],[66,226],[100,226],[100,154],[134,154],[134,66],[226,66],[226,2],[452,2],[452,68],[326,68],[326,122],[422,122],[422,152],[540,152],[540,222],[642,222],[642,254],[672,254]],

[[130,444],[222,444],[222,384],[286,384],[286,288],[414,288],[414,380],[354,380],[354,476],[510,476],[354,476],[354,384],[410,384],[410,288],[514,288],[514,380],[642,380],[642,412],[770,412],[770,608],[882,608],[882,544],[990,544],[990,6],[898,6],[898,58],[990,58],[990,130],[898,130],[898,190],[766,190],[766,258],[642,258],[642,226],[546,226],[546,158],[418,158],[418,130],[322,130],[322,66],[446,66],[446,6],[222,6],[222,66],[130,66],[130,158],[98,158],[98,222],[58,222],[58,418],[158,418],[158,444]],


];

var numero_image_policier=0;

function ennemi(x,y,i) {

this.width= 32;
this.height= 32;
this.state=0;
this.x=x;
this.y=y;

this.draw=function() {

spctx.drawImage(
            personnagesTiles,
            policiers[numero_image_policier][0],
            policiers[numero_image_policier][1] + this.state*32, 
            this.width,
            this.height,
            this.x,
            this.y,
            this.width,
            this.height
        );

};

this.move=function(){

startx=paths[i-1][positioninpaths[i-1]][0];
starty=paths[i-1][positioninpaths[i-1]][1];
endx=paths[i-1][positioninpaths[i-1]+1][0];
endy=paths[i-1][positioninpaths[i-1]+1][1];



if (startx<endx) {this.x +=1;this.state=2;numero_image_policier++}
if (startx>endx) {this.x -=1;this.state=1;numero_image_policier++}
if (starty<endy) {this.y +=1;this.state=0;numero_image_policier++}
if (starty>endy) {this.y -=1;this.state=3;numero_image_policier++}

if (numero_image_policier==5) {numero_image_policier=0};

if (this.x==endx && this.y==endy) {

positioninpaths[i-1] +=1;
if (positioninpaths[i-1] == paths[i-1].length-1) {positioninpaths[i-1]=0;};

}

}

}

var ennemi1 = new ennemi(paths[0][positioninpaths[0]][0],paths[0][positioninpaths[0]][1],1);

var ennemi2 = new ennemi(paths[1][positioninpaths[1]][0],paths[1][positioninpaths[1]][1],2);

var ennemi3 = new ennemi(paths[2][positioninpaths[2]][0],paths[2][positioninpaths[2]][1],3);


var ennemis=[ennemi1,ennemi2,ennemi3];
//remplace myTimer
function animFrame() {
    requestAnimationFrame(animFrame,spcanvas);
    run();
}

animFrame();
//var myTimer=setInterval(run, 40);

window.onload = init();
