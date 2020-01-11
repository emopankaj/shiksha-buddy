<template>
    <draggable v-model="menuStructure" draggable=".item" :group="{ name: 'g1' }">
        <b-row class="align-items-center">
            <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0" v-for="firstOrderMenu in menuStructure">
                <b-button block variant="outline-primary"
                          class="item mt-2" @click="() => editMenuItem(firstOrderMenu)">
                    {{firstOrderMenu.label}}
                </b-button>
                <template v-for="secondOrderMenu in firstOrderMenu.menus">
                    <b-button block variant="warning"
                              class="item mt-2 ml-4 w-fill-available" @click="() => editMenuItem(secondOrderMenu)">
                        {{secondOrderMenu.label}}
                    </b-button>
                    <b-button v-for="thirdOrderMenu in secondOrderMenu.menus" block variant="danger"
                              class="item mt-2 ml-5 w-fill-available" @click="() => editMenuItem(thirdOrderMenu)">
                        {{thirdOrderMenu.label}}
                    </b-button>
                </template>
            </b-col>
        </b-row>
    </draggable>
</template>

<script>
    import draggable from "vuedraggable";
    import {EventBus} from "@/main";

    export default {
        name: "nested-draggable",
        components: {
            draggable
        },
        props: {
            menu: {
                required: true,
                type: Array
            }
        },
        data() {
            return {menuStructure: this.menu}
        },
        methods: {
            editMenuItem(currentMenuItem) {
                EventBus.$emit('edit-menu-item', currentMenuItem);
            }
        }


    };
</script>

<style scoped>
    .w-fill-available {
        width: -webkit-fill-available;
    }
</style>
