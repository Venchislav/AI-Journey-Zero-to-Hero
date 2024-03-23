% create vector
a = [1 2 3];
disp(a);

% Create Matrix
A = [1 2 3; 4 5 6; 7 8 9];
disp(A);

% Print out transposed Matrix
disp(A');

% multiply matrix by transposed vector
disp(A * a');

% multiply matrix by transposed vector
disp(A * a');

B = inv(A);
disp(A * B);

% determinant calculation

disp(det(A));