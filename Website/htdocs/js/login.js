// WARNING: THIS IS NOT SECURE IN ANY FORM!
// TODO: DB FOR ALL LOGINS

const signInBtn = document.getElementById("signInBtn");
const goBackBtn = document.getElementById("goBackBtn");
const userLoginInput = document.getElementById("userLoginInput");
const userPwdInput = document.getElementById("userPwdInput");

const accountsB64 = [
  { user: 'Qnl0M3o=', pwd: 'VGFiYWphcmFAMTIwNzg5NA==' },
  { user: 'Qnl0M3o=', pwd: 'Y3VfYWdhaW4=' },
  { user: 'R2l2Rk5a', pwd: 'R2l2Rk5aMTIzNA==' }
];

// WARNING: BASE64URL ENCODED! WILL BREAK IN SOME BROWSERS
const gDURL1 = "aHR0cHM6Ly9kcml2";
const gDURL2 = "ZS5nb29nbGUuY29t";
const gDURL3 = "L2RyaXZlL2ZvbGRl";
const gDURL4 = "cnMvMURNc2Nkdzkx";
const gDURL5 = "OW5icnphTzVFREQw";
const gDURL6 = "SkR0RnE0VE1sRHVp";
const gDriveURLB64 = gDURL1 + gDURL2 + gDURL3 + gDURL4 + gDURL5 + gDURL6;

function checkUser(user, pwd) {
  const validAcc = accountsB64.find(acc => atob(acc.user) === user && atob(acc.pwd) === pwd);
  if (validAcc) {
    window.location.href = atob(gDriveURLB64);
  } else {
    alert("Username or password is incorrect.");
    location.reload();
  }
};

signInBtn.addEventListener("click", () => {
  const username = userLoginInput.value;
  const password = userPwdInput.value;
  if ((username == "" || password == "") || (username == "" && password == "")) {
    alert("Login details are incomplete. Please try again.")
  } else {
    checkUser(username, password);
  }
});

goBackBtn.addEventListener("click", () => {
  history.back();
});