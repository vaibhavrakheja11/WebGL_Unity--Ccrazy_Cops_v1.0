using UnityEngine;
using System.Collections.Generic;


public class LightEffect : MonoBehaviour {
    
    
    public Animator animator;

    public void Start(){

    }
    public void Update(){

        if(Input.GetKeyDown(KeyCode.L))
        {
            animator.enabled = !animator.enabled;
        }

    }

}