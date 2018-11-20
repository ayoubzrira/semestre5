//commentaire
//clc; clf; clear
A=ones(3,4)

//fonction carre
function d = carre(x)
    d = x .* x
endfunction

//tracé de courbes sur l interval [-10,10]

subplot(1,2,1)
n=10
dx = 1/(n-1)
x = -10:dx:10
plot(x,sin(x),'r-')
xtitle('Graphe de la fonction sin')
legend('x','sin(x)')
xlabel('x'); ylabel('f(x)');

subplot(1,2,2)
n=10
dx = 1/(n-1)
x = -10:dx:10
plot(x,cos(x),'g:')
xtitle('Graphe de la fonction sin')
legend('x','cos(x)')
xlabel('x'); ylabel('f(x)');


figure()

//tracé de la courbe sin sur l interval [0,2pi]
subplot(1,2,1)
n=10
dx = 6
x = 0:dx:2*%pi
plot(x,sin(x),'r--')
xtitle('Graphe de la fonction sin avec dx = 6 ')
legend('x','sin(x)')
xlabel('x'); ylabel('f(x)');

subplot(1,2,2)
n=10
dx = 21
x = 0:dx:2*%pi
plot(x,sin(x),'b-')
xtitle('Graphe de la fonction sin avec dx = 21')
legend('x','sin(x)')
xlabel('x'); ylabel('f(x)');
