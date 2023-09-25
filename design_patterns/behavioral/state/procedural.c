#include <stdio.h>

// Define the states as enumerated values
enum States {
    STATE_INITIAL,
    STATE_GREEN,
    STATE_YELLOW,
    STATE_RED
};

// Define the state machine structure
struct StateMachine {
    enum States current_state;
};

// Function prototypes for state handler functions
void handleInitial(struct StateMachine *machine);
void handleGreen(struct StateMachine *machine);
void handleYellow(struct StateMachine *machine);
void handleRed(struct StateMachine *machine);

// Function pointer type for state handler functions
typedef void (*StateHandler)(struct StateMachine *);

// State transition table
StateHandler state_transitions[] = {
    handleInitial,
    handleGreen,
    handleYellow,
    handleRed
};

// State handler functions
void handleInitial(struct StateMachine *machine) {
    printf("Initial state\n");
    machine->current_state = STATE_GREEN;
}

void handleGreen(struct StateMachine *machine) {
    printf("Green state\n");
    machine->current_state = STATE_YELLOW;
}

void handleYellow(struct StateMachine *machine) {
    printf("Yellow state\n");
    machine->current_state = STATE_RED;
}

void handleRed(struct StateMachine *machine) {
    printf("Red state\n");
    machine->current_state = STATE_GREEN;
}

int main() {
    struct StateMachine machine;
    machine.current_state = STATE_INITIAL;

    while (1) {
        // Call the current state's handler function
        state_transitions[machine.current_state](&machine);
    }

    return 0;
}
