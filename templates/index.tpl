<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Data Theorem Python Coding Exercise: Enter App name</title>
            <style type="text/css">
                .centerDiv
                {
                  width: 800px;
                  height: 100px;
                  position: fixed;
                  top: 50%;
                  left: 50%;
                  margin-top: -100px;
                  margin-left: -300px;
                }

                .input-field {
                  width: 400px;
                  margin-right: 10px;
                  height: 40px;
                  padding: 10px 32px;
                  font-size: 20px;
                }

                .btn {
                  height: 62px;
                  width: 120px;
                  background: #4272d7;
                  white-space: nowrap;
                  border-radius: .5px;
                  padding: 10px 32px;
                  font-size: 20px;
                  color: #fff;
                  transition: all .2s ease-out, color .2s ease-out;
                  border: 0;
                  cursor: pointer;
                }
            </style>
    </head>
    <body>
        <div class="centerDiv">
            <form action="/get-app-info">
                <input class="input-field" type="text" name="appname" placeholder="URL">
                <input class="btn" type="submit" value="Submit">
            </form>
        </div>
    </body>
</html>