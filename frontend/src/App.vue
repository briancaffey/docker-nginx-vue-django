<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/posts">Posts</router-link> |
      <router-link to="/docs">Docs</router-link> |
      <router-link to="/protected">Protected</router-link> |
      <router-link to="/charts">Charts</router-link> |
      <router-link to="/login">Login</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>

::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: white;
    opacity: .5; /* Firefox */
}

:-ms-input-placeholder { /* Internet Explorer 10-11 */
    color: white;
}

::-ms-input-placeholder { /* Microsoft Edge */
    color: white;
}

html {
  background: #2c3e50;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
