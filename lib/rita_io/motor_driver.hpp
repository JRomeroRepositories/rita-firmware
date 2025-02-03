
class MotorDriver {
  public:
    MotorDriver(int pin);
    void motor_turn_on();
    void motor_turn_off();
    void motor_toggle();

  private:
    const int MOTOR_PIN;
};