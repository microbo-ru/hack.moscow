<template>
  <div>
    {{data.name}}
    <hr>
    {{data.region}}
  </div>
</template>

<script>
export default {
  name: "Person",
  props: ["data"]
}
</script>