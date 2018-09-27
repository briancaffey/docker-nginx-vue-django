<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Sign in</h1>
      <label >
        User Name
      </label>
      <input v-model="username" id="username" class="input-box" type="text" placeholder="Username">
      <br>
      <label>
        Password
      </label>
      <input required v-model="password" class="input-box" type="password" placeholder="Password" >
      <hr/>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data(){
    return {
      message: "Hello",
      username: "",
      password: "",
    }
  },
  mounted(){
    document.getElementById('username').focus();
  },
  methods: {
    login(){
      alert(
        "Attempting to login " +
        this.username +
        " with password " +
        this.password
      )
    }
  }
}
</script>

<style scoped>
  .input-box {
    border: 5px red
  }
</style>
